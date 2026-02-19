from db_config import SessionLocal
from sqlalchemy import text

def inspect_farm_schema():
    db = SessionLocal()
    try:
        # Get column names and types for main_farm
        result = db.execute(text("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'main_farm'")).fetchall()
        print("\n--- Columns in main_farm ---")
        for row in result:
            print(f"{row[0]}: {row[1]}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    inspect_farm_schema()
