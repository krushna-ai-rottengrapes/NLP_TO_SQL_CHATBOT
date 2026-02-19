# API Documentation

## Base URL
`http://localhost:8000`

---

## Plans API

### Create Plan
**POST** `/plans/`
```json
{
  "name": "Basic Plan",
  "total_query_allowed": 1000,
  "tokens": 50000,
  "users": 5
}
```

### Get All Plans
**GET** `/plans/?skip=0&limit=100`

### Get Plan by ID
**GET** `/plans/{plan_id}`

### Update Plan
**PUT** `/plans/{plan_id}`
```json
{
  "total_query_allowed": 2000
}
```

### Delete Plan
**DELETE** `/plans/{plan_id}`

---

## Clients API

### Create Client
**POST** `/clients/`
```json
{
  "client_name": "Acme Corp",
  "mobile_number": "+1234567890",
  "email": "contact@acme.com",
  "company_details": "Software company",
  "plan_id": 1
}
```

### Get All Clients
**GET** `/clients/?skip=0&limit=100`

### Get Client by ID
**GET** `/clients/{client_id}`

### Update Client
**PUT** `/clients/{client_id}`
```json
{
  "mobile_number": "+0987654321"
}
```

### Delete Client
**DELETE** `/clients/{client_id}`

---

## Databases API

### Create Database
**POST** `/databases/`
```json
{
  "client_id": 1,
  "provider": "postgres",
  "port": 5432,
  "host": "localhost",
  "user": "dbuser",
  "password": "dbpass",
  "db_name": "mydb",
  "description": {"tables": ["users", "orders"]},
  "db_description": "Production database",
  "private_columns": {"users": ["password", "ssn"]}
}
```

### Test Database Connection
**POST** `/databases/test-connection`
```json
{
  "provider": "postgres",
  "port": 5432,
  "host": "localhost",
  "user": "dbuser",
  "password": "dbpass",
  "db_name": "mydb"
}
```
**Response:**
```json
{
  "status": "success",
  "message": "Connection successful",
  "tables": ["users", "orders", "products"],
  "schema": {
    "users": [
      {"column": "id", "type": "integer"},
      {"column": "name", "type": "varchar"}
    ]
  }
}
```

### Get All Databases
**GET** `/databases/?skip=0&limit=100`

### Get Databases by Client
**GET** `/databases/client/{client_id}`

### Get Database by ID
**GET** `/databases/{database_id}`

### Update Database
**PUT** `/databases/{database_id}`
```json
{
  "port": 5433
}
```

### Delete Database
**DELETE** `/databases/{database_id}`

---

## Users API

### Create User
**POST** `/users/`
```json
{
  "client_id": 1,
  "username": "user@example.com",
  "password": "securepass123",
  "role": "client_user",
  "user_details": {"first_name": "John", "last_name": "Doe"}
}
```

### Get All Users
**GET** `/users/?skip=0&limit=100`

### Get User by ID
**GET** `/users/{user_id}`

### Update User
**PUT** `/users/{user_id}`
```json
{
  "password": "newpassword123"
}
```

### Delete User
**DELETE** `/users/{user_id}`

---

## Query Logs API

### Create Query Log
**POST** `/query-logs/`
```json
{
  "client_id": 1,
  "user_id": 1,
  "query_text": "SELECT * FROM users",
  "total_tokens": 150,
  "retry_tokens": 20
}
```

### Get All Query Logs
**GET** `/query-logs/?skip=0&limit=100`

### Get Query Logs by Client
**GET** `/query-logs/client/{client_id}?skip=0&limit=100`

### Get Query Log by ID
**GET** `/query-logs/{query_log_id}`

---

## Saved Dashboards API

### Create Dashboard
**POST** `/dashboards/`
```json
{
  "client_id": 1,
  "chats": [{"message": "Hello", "response": "Hi"}],
  "charts": [{"type": "bar", "data": [1, 2, 3]}]
}
```

### Get All Dashboards
**GET** `/dashboards/?skip=0&limit=100`

### Get Dashboards by Client
**GET** `/dashboards/client/{client_id}`

### Get Dashboard by ID
**GET** `/dashboards/{dashboard_id}`

### Update Dashboard
**PUT** `/dashboards/{dashboard_id}`
```json
{
  "charts": [{"type": "line", "data": [4, 5, 6]}]
}
```

### Delete Dashboard
**DELETE** `/dashboards/{dashboard_id}`

---

## Enums

### UserRole
- `client`
- `client_user`
- `internal_superuser`

### DBProvider
- `mysql`
- `postgres`
- `mssql`

---

## Setup Instructions

1. Set `DATABASE_URL` in `.env` file
2. Run `pip install -r requirements.txt`
3. Start server: `python main.py`
4. Database tables will be created automatically on startup
