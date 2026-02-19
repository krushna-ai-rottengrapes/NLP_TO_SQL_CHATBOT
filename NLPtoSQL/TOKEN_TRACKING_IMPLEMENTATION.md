# LLM Token Tracking Implementation

## Overview
Added real-time LLM token usage tracking from Groq API responses across all endpoints.

---

## Changes Made

### 1. `query_engine.py` - Core Token Tracking

#### Modified Methods:

**`classify_intent(question)` → Returns `(intent, token_usage)`**
```python
# Now extracts actual token usage from LLM response
if hasattr(intent_response_obj, 'response_metadata'):
    usage = intent_response_obj.response_metadata.get('token_usage', {})
    token_usage = {
        "prompt_tokens": usage.get('prompt_tokens', 0),
        "completion_tokens": usage.get('completion_tokens', 0),
        "total_tokens": usage.get('total_tokens', 0)
    }
```

**`generate_query(question)` → Returns `(sql, tables, schema, token_usage)`**
```python
# Tracks tokens for both table selection and SQL generation
token_usage = {
    "table_selection": {
        "prompt_tokens": ...,
        "completion_tokens": ...,
        "total_tokens": ...
    },
    "sql_generation": {
        "prompt_tokens": ...,
        "completion_tokens": ...,
        "total_tokens": ...
    }
}
```

**`fix_sql_query(query, error, schema)` → Returns `(fixed_query, token_usage)`**
```python
# Tracks tokens used for SQL error correction
token_usage = {
    "prompt_tokens": ...,
    "completion_tokens": ...,
    "total_tokens": ...
}
```

**`process_query(question)` - Main Entry Point**
```python
# Aggregates all token usage and returns in response
response_data = {
    "llm_token_usage": {
        "intent_classification": {...},
        "table_selection": {...},
        "sql_generation": {...},
        "total_tokens_used": 1250  # Sum of all
    }
}
```

---

### 2. `connection.py` - API Response Updates

#### `/query` Endpoint
**Response now includes:**
```json
{
  "status": "success",
  "intent": "sql_query",
  "question": "Show me all customers",
  "sql_query": "SELECT * FROM crm_customer",
  "llm_token_usage": {
    "intent_classification": {
      "prompt_tokens": 450,
      "completion_tokens": 5,
      "total_tokens": 455
    },
    "table_selection": {
      "prompt_tokens": 320,
      "completion_tokens": 12,
      "total_tokens": 332
    },
    "sql_generation": {
      "prompt_tokens": 580,
      "completion_tokens": 25,
      "total_tokens": 605
    },
    "total_tokens_used": 1392
  }
}
```

#### `/execute-sql` Endpoint
**Response now includes retry token tracking:**
```json
{
  "status": "success",
  "data": [...],
  "retry_count": 2,
  "retry_token_usage": [
    {
      "attempt": 1,
      "error": "column 'city' does not exist",
      "tokens": {
        "prompt_tokens": 650,
        "completion_tokens": 30,
        "total_tokens": 680
      }
    },
    {
      "attempt": 2,
      "error": "syntax error near 'WHERE'",
      "tokens": {
        "prompt_tokens": 670,
        "completion_tokens": 28,
        "total_tokens": 698
      }
    }
  ]
}
```

#### `/query-and-execute` Endpoint
**Combines both query and execution token tracking:**
```json
{
  "status": "success",
  "intent": "sql_query",
  "sql_query": "SELECT * FROM crm_customer WHERE city = 'Mumbai'",
  "data": [...],
  "llm_token_usage": {
    "intent_classification": {...},
    "table_selection": {...},
    "sql_generation": {...},
    "sql_fix_retries": [
      {
        "attempt": 1,
        "error": "...",
        "tokens": {...}
      }
    ],
    "total_tokens_used": 2150
  }
}
```

---

## Token Usage Breakdown

### Per Chain Token Tracking:

1. **Intent Classification Chain**
   - Prompt: User question + conversation context + system prompt
   - Completion: Single word (SQL_QUERY, CASUAL_CHAT, etc.)
   - Typical: 400-500 prompt tokens, 5-10 completion tokens

2. **Table Selection Chain**
   - Prompt: User question + table catalog + context
   - Completion: JSON array of table names
   - Typical: 300-400 prompt tokens, 10-20 completion tokens

3. **SQL Generation Chain**
   - Prompt: User question + filtered schema + context + chat history
   - Completion: SQL query
   - Typical: 500-800 prompt tokens, 20-50 completion tokens

4. **SQL Fix Chain** (only on errors)
   - Prompt: Failed query + error message + schema
   - Completion: Corrected SQL query
   - Typical: 600-700 prompt tokens, 25-40 completion tokens

---

## How to Use Token Data

### 1. Store in Database
```python
# Example schema
token_logs = {
    "session_id": "session_20240115_143022",
    "question": "Show me all customers",
    "intent": "sql_query",
    "timestamp": "2024-01-15T14:30:25",
    "intent_tokens": 455,
    "table_selection_tokens": 332,
    "sql_generation_tokens": 605,
    "sql_fix_tokens": 0,
    "total_tokens": 1392,
    "retry_count": 0
}
```

### 2. Calculate Costs
```python
# Groq pricing (example)
PROMPT_TOKEN_COST = 0.00001  # $0.01 per 1K tokens
COMPLETION_TOKEN_COST = 0.00003  # $0.03 per 1K tokens

def calculate_cost(token_usage):
    prompt_cost = token_usage['prompt_tokens'] * PROMPT_TOKEN_COST / 1000
    completion_cost = token_usage['completion_tokens'] * COMPLETION_TOKEN_COST / 1000
    return prompt_cost + completion_cost

total_cost = calculate_cost(response['llm_token_usage']['intent_classification'])
```

### 3. Monitor Usage
```python
# Track daily token consumption
daily_tokens = sum(log['total_tokens'] for log in token_logs_today)
daily_cost = calculate_total_cost(token_logs_today)

# Alert if exceeding budget
if daily_cost > DAILY_BUDGET:
    send_alert("Token budget exceeded!")
```

### 4. Optimize Prompts
```python
# Identify expensive chains
avg_tokens_by_chain = {
    "intent": avg([log['intent_tokens'] for log in logs]),
    "table_selection": avg([log['table_selection_tokens'] for log in logs]),
    "sql_generation": avg([log['sql_generation_tokens'] for log in logs])
}

# Focus optimization on highest token consumers
```

---

## Benefits

1. **Accurate Cost Tracking**: Real token counts from LLM, not estimates
2. **Per-Chain Visibility**: See which step uses most tokens
3. **Retry Cost Tracking**: Monitor token usage during error correction
4. **Database Ready**: All data structured for easy storage
5. **Budget Management**: Set alerts based on actual usage
6. **Optimization Insights**: Identify expensive operations

---

## Example Response Flow

### User Query: "Show me customers in Mumbai"

**Step 1: Intent Classification**
- Prompt Tokens: 450
- Completion Tokens: 5
- Total: 455

**Step 2: Table Selection**
- Prompt Tokens: 320
- Completion Tokens: 12
- Total: 332

**Step 3: SQL Generation**
- Prompt Tokens: 580
- Completion Tokens: 25
- Total: 605

**Step 4: SQL Execution** (fails)
- Error: "column 'city' does not exist"

**Step 5: SQL Fix (Retry 1)**
- Prompt Tokens: 650
- Completion Tokens: 30
- Total: 680

**Step 6: SQL Execution** (success!)

**Total Tokens Used: 2,072**
- Query Generation: 1,392
- Error Correction: 680

---

## Database Schema Suggestion

```sql
CREATE TABLE llm_token_logs (
    id SERIAL PRIMARY KEY,
    session_id VARCHAR(100),
    question TEXT,
    intent VARCHAR(50),
    timestamp TIMESTAMP DEFAULT NOW(),
    
    -- Token breakdown
    intent_prompt_tokens INT,
    intent_completion_tokens INT,
    intent_total_tokens INT,
    
    table_selection_prompt_tokens INT,
    table_selection_completion_tokens INT,
    table_selection_total_tokens INT,
    
    sql_generation_prompt_tokens INT,
    sql_generation_completion_tokens INT,
    sql_generation_total_tokens INT,
    
    -- Retry tracking
    retry_count INT DEFAULT 0,
    retry_total_tokens INT DEFAULT 0,
    
    -- Totals
    total_prompt_tokens INT,
    total_completion_tokens INT,
    total_tokens INT,
    
    -- Cost (calculated)
    estimated_cost DECIMAL(10, 6)
);

-- Index for analytics
CREATE INDEX idx_session_timestamp ON llm_token_logs(session_id, timestamp);
CREATE INDEX idx_intent ON llm_token_logs(intent);
```

---

## Next Steps

1. **Add logging middleware** to automatically save token usage
2. **Create analytics dashboard** to visualize token consumption
3. **Set up cost alerts** when approaching budget limits
4. **Optimize expensive prompts** based on token data
5. **A/B test prompt variations** to reduce token usage

---

## End of Documentation

## My notes from ChatGPT
1) Where memory lives (high-level)
In your code memory is implemented by the ConversationMemory class and an instance of it is stored inside each QueryEngine as self.memory. Runtime flow:

When a user sends a question, process_query() calls self.memory.add_message("user", question).

After the LLM produces an answer the code calls self.memory.add_message("assistant", response, metadata=...).

The memory instance is consulted when producing prompts: self.memory.get_context_summary() and self.memory.get_langchain_messages() are passed into prompt templates and chains so the LLM can see recent context.

So memory = in-memory deque of recent messages + helper methods to format and summarize those messages for the LLM.