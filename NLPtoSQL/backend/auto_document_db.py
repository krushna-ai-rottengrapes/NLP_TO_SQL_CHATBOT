"""
AI Auto-Documentation Script
=============================
Scans ONLY the user-selected tables, reads 3 sample rows,
and uses the LLM (Groq Llama-3) to auto-generate descriptions
for each table and its columns.

Usage:
    python auto_document_db.py

It will:
1. Ask for a database_id (from your saved connections).
2. Read the selected_tables list from the databases record.
3. For each selected table:
   - Fetch 3 rows of actual data.
   - Ask the AI to explain what the table & columns are.
4. Save the AI-generated descriptions to the databases.description JSON column.
"""

import os
import sys
import json
import psycopg2
import pymysql
from dotenv import load_dotenv
from sqlalchemy.orm import Session

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

from db_config import SessionLocal
from database.models import Database as DBModel
from utils.encryption import decrypt_password
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def get_db_session():
    """Get a database session"""
    db = SessionLocal()
    try:
        return db
    except Exception:
        db.close()
        raise


def get_sample_data(db_record, plain_password, table_name, limit=3):
    """Fetch sample rows from a table using direct connection"""
    try:
        if db_record.provider.value == "postgres":
            conn = psycopg2.connect(
                host=db_record.host,
                port=db_record.port,
                database=db_record.db_name,
                user=db_record.user,
                password=plain_password
            )
        elif db_record.provider.value == "mysql":
            conn = pymysql.connect(
                host=db_record.host,
                port=db_record.port,
                database=db_record.db_name,
                user=db_record.user,
                password=plain_password
            )
        else:
            print(f"  ⚠️  Unsupported provider: {db_record.provider.value}")
            return None, None

        cursor = conn.cursor()

        # Get column names
        if db_record.provider.value == "postgres":
            cursor.execute(f"""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = '{table_name}' AND table_schema = 'public'
                ORDER BY ordinal_position
            """)
        else:
            cursor.execute(f"""
                SELECT column_name, data_type 
                FROM information_schema.columns 
                WHERE table_name = '{table_name}'
                ORDER BY ordinal_position
            """)

        columns_info = cursor.fetchall()
        column_names = [c[0] for c in columns_info]
        column_types = {c[0]: c[1] for c in columns_info}

        if not column_names:
            cursor.close()
            conn.close()
            return None, None

        # Fetch sample rows
        cursor.execute(f'SELECT * FROM "{table_name}" LIMIT {limit}')
        rows = cursor.fetchall()

        # Convert to list of dicts
        sample_data = []
        for row in rows:
            row_dict = {}
            for col_name, val in zip(column_names, row):
                # Convert non-serializable types to string
                try:
                    json.dumps(val)
                    row_dict[col_name] = val
                except (TypeError, ValueError):
                    row_dict[col_name] = str(val)
            sample_data.append(row_dict)

        cursor.close()
        conn.close()

        return column_types, sample_data

    except Exception as e:
        print(f"  ❌ Error fetching data from '{table_name}': {e}")
        return None, None


def analyze_table_with_ai(llm, table_name, column_types, sample_data):
    """Use LLM to analyze a table and generate a description"""

    # Build column info string
    col_info = "\n".join([f"  - {name} ({dtype})" for name, dtype in column_types.items()])

    # Build sample data string (limit to avoid token overflow)
    sample_str = ""
    for i, row in enumerate(sample_data):
        row_preview = {k: (str(v)[:50] if isinstance(v, str) and len(str(v)) > 50 else v) for k, v in row.items()}
        sample_str += f"  Row {i+1}: {json.dumps(row_preview, default=str)}\n"

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a Database Documentation Expert.
Analyze the table structure and sample data below.
Generate a clear, concise description of what this table stores and what its key columns represent.

IMPORTANT: Output ONLY valid JSON. No markdown, no extra text.
Format:
{{
  "description": "One sentence explaining what this table stores.",
  "columns": {{
    "column_name": "What this column represents"
  }}
}}"""),
        ("human", """Table Name: {table_name}

Columns:
{col_info}

Sample Data ({num_rows} rows):
{sample_data}

Analyze this table and generate descriptions.""")
    ])

    chain = prompt | llm | StrOutputParser()

    try:
        result = chain.invoke({
            "table_name": table_name,
            "col_info": col_info,
            "num_rows": len(sample_data),
            "sample_data": sample_str
        })

        # Clean result and parse JSON
        result = result.strip()
        if result.startswith("```"):
            result = result.split("\n", 1)[1]  # Remove first line
            result = result.rsplit("```", 1)[0]  # Remove last ```
            result = result.strip()

        parsed = json.loads(result)
        return parsed

    except json.JSONDecodeError as e:
        print(f"  ⚠️  JSON parse error for '{table_name}': {e}")
        print(f"  Raw output: {result[:200]}")
        # Return a basic fallback
        return {
            "description": f"Table '{table_name}' (AI could not parse, manual review needed)",
            "columns": {}
        }
    except Exception as e:
        print(f"  ❌ LLM error for '{table_name}': {e}")
        return None


def main():
    print("=" * 60)
    print("🤖 AI Auto-Documentation Script")
    print("=" * 60)
    print()

    # Connect to backend DB
    db = get_db_session()

    # List available databases
    databases = db.query(DBModel).all()
    if not databases:
        print("❌ No databases found. Please add a connection in the UI first.")
        db.close()
        return

    print("📋 Available Database Connections:")
    for d in databases:
        table_count = len(d.selected_tables) if d.selected_tables else 0
        print(f"  [{d.id}] {d.db_name} ({d.provider.value}) - {table_count} tables selected")

    print()
    try:
        db_id = int(input("Enter database ID to scan: "))
    except (ValueError, EOFError):
        print("Invalid input. Exiting.")
        db.close()
        return

    # Get the database record
    db_record = db.query(DBModel).filter(DBModel.id == db_id).first()
    if not db_record:
        print(f"❌ Database ID {db_id} not found.")
        db.close()
        return

    # Get selected tables
    selected_tables = db_record.selected_tables or []
    if not selected_tables:
        print("❌ No tables selected! Please select tables in the Frontend UI first.")
        db.close()
        return

    print(f"\n🎯 Database: {db_record.db_name}")
    print(f"📊 Selected Tables: {len(selected_tables)}")
    print(f"📝 Tables: {', '.join(selected_tables[:10])}{'...' if len(selected_tables) > 10 else ''}")
    print()

    confirm = input(f"Scan {len(selected_tables)} tables with AI? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Cancelled.")
        db.close()
        return

    # Decrypt password
    plain_password = decrypt_password(db_record.password)

    # Initialize LLM
    print("\n🧠 Initializing AI (Groq Llama-3)...")
    llm = ChatGroq(
        temperature=0,
        model_name="llama-3.3-70b-versatile"
    )

    # Get existing descriptions (to preserve manual ones)
    existing_descriptions = db_record.description or {}

    # Process each table
    total = len(selected_tables)
    success = 0
    failed = 0

    print(f"\n🔍 Starting AI scan of {total} tables...\n")

    for i, table_name in enumerate(selected_tables):
        print(f"[{i+1}/{total}] Scanning: {table_name}...")

        # Skip if already has a description (unless it's empty)
        if table_name in existing_descriptions:
            existing = existing_descriptions[table_name]
            if isinstance(existing, dict) and existing.get("description"):
                print(f"  ⏭️  Already has description. Skipping. (Use --force to override)")
                success += 1
                continue

        # Fetch sample data
        column_types, sample_data = get_sample_data(db_record, plain_password, table_name)

        if column_types is None or sample_data is None:
            print(f"  ⚠️  No data found. Skipping.")
            failed += 1
            continue

        if len(sample_data) == 0:
            print(f"  ⚠️  Table is empty. Using column names only.")
            sample_data = [{"(empty table)": "no data"}]

        # Ask AI
        result = analyze_table_with_ai(llm, table_name, column_types, sample_data)

        if result:
            existing_descriptions[table_name] = result
            print(f"  ✅ {result.get('description', 'Done')[:80]}")
            success += 1
        else:
            failed += 1

    # Save all descriptions back to DB
    print(f"\n💾 Saving descriptions to database...")
    db_record.description = existing_descriptions
    db.commit()

    print(f"\n{'=' * 60}")
    print(f"✅ DONE!")
    print(f"   Scanned: {total} tables")
    print(f"   Success: {success}")
    print(f"   Failed:  {failed}")
    print(f"{'=' * 60}")
    print(f"\n🎉 Your Chatbot is now smarter! Try asking a question.")

    db.close()


if __name__ == "__main__":
    main()
