# Geo-Query Debugging Summary

## Current Issue
**404 "City geometry not found for 'Nadipura'"** persists after 5 patches adding:
- Place text cleanup (suffix stripping)
- SQLAlchemy 2.x compatibility fix
- Schema normalization
- Aggregated geometry fallback (ST_UnaryUnion)
- Fuzzy matching (exact + normalized + ILIKE)

## Root Cause: Unknown (System + DB Mismatch)
Two blockers prevent direct debugging:

### Blocker 1: Windows Application Control Policy
The backend cannot start due to pandas DLL security restrictions:
```
ImportError: DLL load failed while importing nattype: An Application Control policy has blocked this file.
```
This prevents running the backend to test the endpoint directly.

### Blocker 2: Database Password/Encoding Issue
Direct database test script fails with auth:
```
psycopg2.OperationalError: connection to server... password authentication failed for user "postgres"
```
The password `RG@2025databa$e` may have special character encoding issues with the `$` requiring URL escaping.

## Debug Output Added
Added comprehensive logging to `_resolve_city_geometry_from_db()` in [database/connection.py](database/connection.py#L227) that will show:

1. **[GEO DEBUG] Found N geometry column(s)** — Which tables have spatial data
2. **[GEO DEBUG] Attempting table=X, geom_col=Y, name_col=Z** — Which name column being tried
3. **[GEO DEBUG] Direct lookup SQL: [SQL]** — Exact query being executed
4. **[GEO DEBUG] Direct lookup result: [None/data]** — Whether single row found
5. **[GEO DEBUG] Aggregate lookup result: [None/data]** — Whether group aggregate found
6. **[GEO DEBUG] No geometry match in table X, continuing...** — Table skipped, moving to next

Plus test endpoint at `/database/test-geo-resolver` (no auth required) that can be called as:
```json
POST /database/test-geo-resolver
{
  "question": "show records inside Nadipura",
  "database_id": 1
}
```

## Next Steps to Unblock

### Option 1: Bypass Pandas DLL Issue (Recommended)
1. **Uninstall pandas** from the environment
2. **Check if pandas is actually used** in the query_engine — it may not be necessary for geo-query flow
3. **If not used**: Remove the `import pandas as pd` line from [Langchain/query_engine.py](Langchain/query_engine.py#L8)
4. Restart backend

### Option 2: Use System Without Pandas DLL Issue
1. Run backend in WSL (Windows Subsystem for Linux) where there's no AppLocker policy
2. Or run in Docker container
3. Or use different Python version (try 3.12 or 3.11 instead of 3.14)

### Option 3: Disable Windows AppLocker/Security Policy
1. Contact system administrator to whitelist pandas DLLs
2. Or temporarily disable the policy (requires admin)

## Database Credentials Issue
To fix the direct test script, encode the password properly:
```python
from urllib.parse import quote

password = "RG@2025databa$e"
encoded = quote(password, safe='')  # Encodes $ as %24
# Use in URI: postgresql://user:encoded_password@host/db
```

## Current Code Status

### Files Modified
- [backend/database/connection.py](backend/database/connection.py)
  - `_resolve_city_geometry_from_db()`: Added 10+ debug print statements (lines ~225-350)
  - `execute_geo_nlp_query()`: Existing endpoint with geo-query flow (lines ~434-470)
  - New `/database/test-geo-resolver` endpoint: No-auth test endpoint (lines ~970-1050)

### How the Resolver Works
```python
# Current flow
place_name = "Nadipura"  # extracted from question
place_name_cleaned = "Nadipura"  # after suffix cleanup

# Step 1: Find all geometry columns in database
SELECT c.table_schema, c.table_name, c.column_name
FROM information_schema.columns
WHERE udt_name IN ('geometry', 'geography')

# Step 2: For each geometry table, find matching name column
# Tries candidates: city_name, city, name, village, locality, place_name, etc.

# Step 3: Direct lookup - try single-row polygon
SELECT ST_AsGeoJSON(polygon) FROM main_farm
WHERE LOWER(village) = LOWER('Nadipura')
  OR LOWER(REGEXP_REPLACE(village, '[^a-zA-Z0-9]', '', 'g')) = 'nadipura'
  OR LOWER(village) ILIKE '%Nadipura%'
LIMIT 1

# Step 4: If no single row, aggregate all matching rows
SELECT ST_AsGeoJSON(ST_UnaryUnion(polygon)) FROM main_farm
WHERE (... same conditions ...)
  AND polygon IS NOT NULL

# Step 5: Return geometry as GeoJSON or raise 404
```

## Expected Behavior
When backend starts and `/database/test-geo-resolver` is called with `{"question": "show records inside Nadipura", "database_id": 1}`:

**If working:**
```json
{
  "status": "success",
  "message": "Geometry resolved successfully",
  "city": "Nadipura",
  "geometry_type": "Polygon",
  "geometry": { "type": "Polygon", "coordinates": [...] }
}
```

**If not found:**
```json
{
  "status": "error",
  "message": "City geometry not found for 'Nadipura'.",
  "city": "Nadipura",
  "status_code": 404
}
```

**With detailed debug output in terminal showing which table/column/SQL was attempted.**

## Debugging Checklist
Use these checks once backend is running:

1. **Call test endpoint** → see if geometry found or 404
2. **Check console output** → scan for `[GEO DEBUG]` messages to see which table/column was searched
3. **Manual SQL check** in pgAdmin:
   ```sql
   -- Check if geometry columns exist
   SELECT column_name FROM information_schema.columns
   WHERE table_name='main_farm' AND udt_name='geometry';
   
   -- Count rows with village='Nadipura'
   SELECT COUNT(*) FROM main_farm WHERE village='Nadipura';
   
   -- Try direct geometry fetch
   SELECT ST_AsGeoJSON(polygon) FROM main_farm 
   WHERE village='Nadipura' LIMIT 1;
   
   -- Try aggregated geometry
   SELECT ST_AsGeoJSON(ST_UnaryUnion(polygon)) FROM main_farm 
   WHERE village='Nadipura' AND polygon IS NOT NULL;
   ```
4. **Compare results** between manual SQL and what resolver found

## Files to Review
- [backend/database/connection.py](backend/database/connection.py#L227) — Main resolver with debug output
- [backend/Langchain/query_engine.py](backend/Langchain/query_engine.py#L8) — Check if pandas actually used
- [backend/Langchain/query_engine.py](backend/Langchain/query_engine.py#L585) — Schema filtering that passes to resolver

## Summary
The geometry resolver code is now heavily instrumented with debug output. Once the backend can start (by fixing the pandas DLL issue), the test endpoint will reveal exactly which table/column was searched, what SQL returned, and why the 404 is occurring. This will directly point to the root cause:
- Wrong column name priority order?
- Null geometries in the main_farm table?
- Table not being recognized as a geometry table?
- Schema qualification issues?

The answer will be in the `[GEO DEBUG]` console output.
