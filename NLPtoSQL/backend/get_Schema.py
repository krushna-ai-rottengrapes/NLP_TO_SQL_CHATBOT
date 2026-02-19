from sqlalchemy import create_engine, inspect, text
from urllib.parse import quote
from sqlalchemy.exc import ProgrammingError, DBAPIError

# ----------------------------------------------------
# DATABASE CONNECTION
# ----------------------------------------------------
print("🔌 Connecting to database...")

db_user = "rgrapes"
db_password = "RG@2025databa$e"
db_host = "sql01.trackit.aero"
db_name = "entrackx1"
db_port = 1440

encoded_password = quote(db_password, safe="")

engine = create_engine(
    f"mssql+pymssql://{db_user}:{encoded_password}@{db_host}:{db_port}/{db_name}",
    pool_pre_ping=True,
    connect_args={"timeout": 5}
)

inspector = inspect(engine)
print("✅ Connected")

# ----------------------------------------------------
# TARGET VIEWS (ONLY THESE)
# ----------------------------------------------------
TARGET_VIEWS = [
    ("gse", "vwGSEAssets"),
    ("gse", "vwGSEStatus"),
]

# ----------------------------------------------------
# TABLE DDL
# ----------------------------------------------------
def get_table_ddl(schema, table):
    try:
        cols = inspector.get_columns(table, schema=schema)
        ddl = [f"CREATE TABLE [{schema}].[{table}] ("]
        for c in cols:
            line = f"  [{c['name']}] {c['type']}"
            if not c.get("nullable", True):
                line += " NOT NULL"
            ddl.append(line + ",")
        ddl[-1] = ddl[-1].rstrip(",")
        ddl.append(");")
        return "\n".join(ddl)
    except Exception as e:
        return f"-- Table DDL not available: {e}"

# ----------------------------------------------------
# SAMPLE ROWS (TABLES ONLY)
# ----------------------------------------------------
def get_sample_rows(schema, table):
    try:
        with engine.connect() as conn:
            result = conn.execute(
                text(f"SELECT TOP 3 * FROM [{schema}].[{table}]")
            )
            rows = result.fetchall()
            if not rows:
                return "No rows."

            cols = result.keys()
            out = "\t".join(cols) + "\n"
            for r in rows:
                out += "\t".join(str(v) for v in r) + "\n"
            return out
    except (ProgrammingError, DBAPIError):
        return "Sample rows not accessible."
    except Exception as e:
        return f"Error: {e}"

# ----------------------------------------------------
# VIEW DDL
# ----------------------------------------------------
def get_view_ddl(schema, view):
    try:
        with engine.connect() as conn:
            row = conn.execute(
                text("""
                    SELECT m.definition
                    FROM sys.sql_modules m
                    JOIN sys.views v ON m.object_id = v.object_id
                    JOIN sys.schemas s ON v.schema_id = s.schema_id
                    WHERE v.name = :view AND s.name = :schema
                """),
                {"view": view, "schema": schema}
            ).fetchone()

            if row and row[0]:
                return f"CREATE VIEW [{schema}].[{view}] AS\n{row[0]}"
            return "-- View definition not available"
    except Exception:
        return "-- View skipped (timeout / permissions)"

# ----------------------------------------------------
# VIEW COLUMNS
# ----------------------------------------------------
def get_view_columns(schema, view):
    try:
        cols = inspector.get_columns(view, schema=schema)
        lines = [
            "| Column | Type | Nullable |",
            "|--------|------|----------|",
        ]
        for c in cols:
            lines.append(
                f"| {c['name']} | {c['type']} | {'YES' if c.get('nullable', True) else 'NO'} |"
            )
        return "\n".join(lines)
    except Exception as e:
        return f"_Could not fetch columns: {e}_"

# ----------------------------------------------------
# BUILD DOCUMENT
# ----------------------------------------------------
def build_schema_doc():
    output = ["# 📘 Database Schema (Tables + Selected Views)\n"]

    # -------- ALL TABLES --------
    schemas = inspector.get_schema_names()

    for schema in schemas:
        tables = inspector.get_table_names(schema=schema)

        if not tables:
            continue

        print(f"📦 Tables in schema: {schema}")

        output.append(f"\n## 🧱 TABLES – Schema `{schema}`\n")

        for table in tables:
            print(f"   🧱 {schema}.{table}")
            output.append(f"### TABLE: `{schema}.{table}`\n")
            output.append("```sql")
            output.append(get_table_ddl(schema, table))
            output.append("```")
            output.append("Sample Rows:\n```text")
            output.append(get_sample_rows(schema, table))
            output.append("```\n")

    # -------- ONLY 2 VIEWS --------
    output.append("\n## 👁️ SELECTED VIEWS\n")

    for schema, view in TARGET_VIEWS:
        print(f"👁️ View: {schema}.{view}")
        output.append(f"### VIEW: `{schema}.{view}`\n")

        output.append("Columns:\n")
        output.append(get_view_columns(schema, view) + "\n")

        output.append("DDL:\n```sql")
        output.append(get_view_ddl(schema, view))
        output.append("```\n")

    return "\n".join(output)

# ----------------------------------------------------
# EXPORT
# ----------------------------------------------------
def export_file(fmt="md"):
    content = build_schema_doc()
    fname = f"schema_tables_plus_views.{fmt}"

    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Export completed → {fname}")

# ----------------------------------------------------
# RUN
# ----------------------------------------------------
if __name__ == "__main__":
    export_file("md")   # or "txt"
