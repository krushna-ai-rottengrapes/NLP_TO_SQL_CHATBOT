#!/usr/bin/env python
"""Direct test of geo-query resolver without pandas imports."""

import sys
import json
import re
from sqlalchemy import create_engine, text
from urllib.parse import quote

# Simulate the database config
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "nlp_to_sql_db"
DB_USER = "postgres"
DB_PASSWORD = "RG@2025databa$e"

# Build connection URI
def create_connection_uri():
    encoded_password = quote(DB_PASSWORD, safe='')
    return f"postgresql+psycopg2://{DB_USER}:{encoded_password}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def _normalize_place_text(place: str) -> str:
    """Normalize place text for fuzzy matching."""
    return re.sub(r"[^a-zA-Z0-9]", "", place).lower()

def _clean_place_text(place: str) -> str:
    """Clean place text: remove punctuation and locality suffixes."""
    cleaned = place.strip()
    # Remove punctuation
    cleaned = re.sub(r"[.,!?;:'\"—–-]", " ", cleaned)
    # Remove locale suffixes
    cleaned = re.sub(r"'s\s+farm$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+farm$", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s+(?:falia|village|city|town)$", "", cleaned, flags=re.IGNORECASE)
    return cleaned.strip()

def _is_safe_identifier(identifier: str) -> bool:
    """Allow only simple SQL identifiers."""
    return bool(re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", identifier))

def test_resolver():
    """Test the geometry resolver directly."""
    try:
        engine = create_engine(create_connection_uri())
        print("[TEST] Connected to database")
        
        city_name = "Nadipura"
        city_name_cleaned = _clean_place_text(city_name)
        print(f"[TEST] Testing with city_name='{city_name}' → cleaned='{city_name_cleaned}'")
        
        # Step 1: Find geometry columns
        metadata_query = text("""
            SELECT c.table_schema, c.table_name, c.column_name
            FROM information_schema.columns c
            WHERE c.table_schema NOT IN ('information_schema', 'pg_catalog')
              AND (
                c.udt_name IN ('geometry', 'geography')
                OR (c.data_type = 'USER-DEFINED' AND c.udt_name ILIKE '%geom%')
              )
            ORDER BY c.table_schema, c.table_name
        """)
        
        with engine.connect() as conn:
            geometry_columns = conn.execute(metadata_query).fetchall()
            print(f"[TEST] Found {len(geometry_columns)} geometry columns: {geometry_columns}")
            
            if not geometry_columns:
                print("[TEST] ERROR: No geometry columns found!")
                return
            
            name_column_candidates = [
                "city_name", "city", "name", "cityname", "district_name", "district",
                "town_name", "town", "village", "village_name", "locality", "location",
                "area_name", "ward_name", "place_name"
            ]
            normalized_city_name = _normalize_place_text(city_name_cleaned)
            
            # Step 2: For each geometry column, try to find matching name column
            for schema_name, table_name, geom_col in geometry_columns:
                if not all(_is_safe_identifier(x) for x in [schema_name, table_name, geom_col]):
                    print(f"[TEST] Skipping {schema_name}.{table_name}.{geom_col} - unsafe identifier")
                    continue
                
                # Get all columns in this table
                column_query = text("""
                    SELECT column_name
                    FROM information_schema.columns
                    WHERE table_schema = :schema_name AND table_name = :table_name
                """)
                table_columns = [
                    row[0] for row in conn.execute(
                        column_query,
                        {"schema_name": schema_name, "table_name": table_name}
                    ).fetchall()
                ]
                print(f"[TEST] Table {schema_name}.{table_name} columns: {table_columns}")
                
                table_columns_lower = {col.lower(): col for col in table_columns}
                matched_name_col = None
                for candidate in name_column_candidates:
                    if candidate in table_columns_lower:
                        matched_name_col = table_columns_lower[candidate]
                        break
                
                if not matched_name_col:
                    print(f"[TEST] No matching name column in {schema_name}.{table_name}")
                    continue
                
                print(f"[TEST] Using name column: {matched_name_col}")
                
                # Step 3: Try direct lookup
                lookup_sql = text(
                    f'SELECT ST_AsGeoJSON("{geom_col}") AS city_geojson '
                    f'FROM "{schema_name}"."{table_name}" '
                    f'WHERE '
                    f'LOWER(TRIM(CAST("{matched_name_col}" AS TEXT))) = LOWER(TRIM(:city_name)) '
                    f"OR LOWER(REGEXP_REPLACE(TRIM(CAST(\"{matched_name_col}\" AS TEXT)), '[^a-zA-Z0-9]', '', 'g')) = :normalized_city_name "
                    f'OR LOWER(CAST("{matched_name_col}" AS TEXT)) ILIKE :city_like '
                    f'LIMIT 1'
                )
                print(f"[TEST] Direct lookup SQL: {str(lookup_sql)}")
                print(f"[TEST] Parameters: city_name='{city_name_cleaned}', normalized={normalized_city_name}, city_like='%{city_name_cleaned.strip()}%'")
                
                try:
                    result = conn.execute(
                        lookup_sql,
                        {
                            "city_name": city_name_cleaned,
                            "normalized_city_name": normalized_city_name,
                            "city_like": f"%{city_name_cleaned.strip()}%",
                        }
                    ).fetchone()
                    print(f"[TEST] Direct lookup result: {result}")
                    if result and result[0]:
                        print(f"[TEST] ✓ Found geometry!")
                        geometry = json.loads(result[0])
                        print(f"[TEST] Geometry type: {geometry.get('type')}")
                        return
                except Exception as e:
                    print(f"[TEST] Direct lookup error: {e}")
                
                # Step 4: Try aggregate fallback
                aggregate_lookup_sql = text(
                    f'SELECT ST_AsGeoJSON(ST_UnaryUnion("{geom_col}")) AS city_geojson '
                    f'FROM "{schema_name}"."{table_name}" '
                    f'WHERE ('
                    f'LOWER(TRIM(CAST("{matched_name_col}" AS TEXT))) = LOWER(TRIM(:city_name)) '
                    f"OR LOWER(REGEXP_REPLACE(TRIM(CAST(\"{matched_name_col}\" AS TEXT)), '[^a-zA-Z0-9]', '', 'g')) = :normalized_city_name "
                    f'OR LOWER(CAST("{matched_name_col}" AS TEXT)) ILIKE :city_like) '
                    f'AND "{geom_col}" IS NOT NULL'
                )
                print(f"[TEST] Aggregate lookup SQL: {str(aggregate_lookup_sql)}")
                
                try:
                    agg_result = conn.execute(
                        aggregate_lookup_sql,
                        {
                            "city_name": city_name_cleaned,
                            "normalized_city_name": normalized_city_name,
                            "city_like": f"%{city_name_cleaned.strip()}%",
                        }
                    ).fetchone()
                    print(f"[TEST] Aggregate lookup result: {agg_result}")
                    if agg_result and agg_result[0]:
                        geometry = json.loads(agg_result[0])
                        if geometry.get("type") in {"Polygon", "MultiPolygon"}:
                            print(f"[TEST] ✓ Found aggregated geometry!")
                            return
                except Exception as e:
                    print(f"[TEST] Aggregate lookup error: {e}")
                
                print(f"[TEST] No geometry in {schema_name}.{table_name}, continuing...")
            
            print(f"[TEST] ✗ No geometry found after checking all tables")
    
    except Exception as e:
        print(f"[TEST] FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_resolver()
