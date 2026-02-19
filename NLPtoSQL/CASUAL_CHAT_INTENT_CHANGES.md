# Casual Chat Intent Implementation

## Overview
Added support for handling casual conversation queries (greetings, personal questions, etc.) with a new `CASUAL_CHAT` intent type.

## Changes Made

### 1. Backend - Query Engine (`backend/Langchain/query_engine.py`)

#### Intent Enum
- Renamed `GENERAL_KNOWLEDGE` to `CASUAL_CHAT` for clarity
- Updated enum definition to only include: `SQL_QUERY`, `CASUAL_CHAT`, `SARCASTIC_RESPONSE`, `AMBIGUOUS`

#### Intent Classification Prompt
- Updated system prompt to classify casual greetings and personal questions as `CASUAL_CHAT`
- Examples: "hi", "hello", "how are you", "who are you", "what's your name", "what time is it", "where do you stay", "what's your gender", "who is your boss"

#### Intent Detection Logic
- Updated `classify_intent()` method to check for `CASUAL_CHAT` instead of `GENERAL_KNOWLEDGE`

#### Handler Method
- Renamed `handle_general_knowledge()` to `handle_casual_chat()`
- Maintains same functionality: performs web search and returns conversational response

#### Query Processing
- Updated `process_query()` to handle `QueryIntent.CASUAL_CHAT`
- Stores casual chat responses in conversation memory with `intent: "casual_chat"` metadata

### 2. Backend - Connection Routes (`backend/database/connection.py`)

#### Query Endpoints
- Updated `/database/query` endpoint to check for `casual_chat` intent
- Updated `/database/query-and-execute` endpoint to check for `casual_chat` intent

#### Intent Testing
- Updated `/database/test-intent` endpoint with new intent descriptions
- Changed description from "Factual question - Web search" to "Casual conversation - Web search"

### 3. Frontend - Chat Message Display (`frontend/src/app/components/ChatMessage.jsx`)

#### Intent Color Mapping
- Updated `intentColors` object to use `casual_chat` instead of `general_knowledge`
- Maintains green color scheme for casual chat responses (bg-green-100, text-green-800)

## Response Flow

### When user asks a casual question (e.g., "Hi, how are you?"):

1. **Intent Classification**: LLM classifies as `CASUAL_CHAT`
2. **Web Search**: System performs web search for context
3. **Response Generation**: Returns conversational response
4. **Frontend Display**: Shows green badge with "CASUAL CHAT" label
5. **Memory Storage**: Stores in conversation history for context

### Response Structure:
```json
{
  "status": "success",
  "intent": "casual_chat",
  "question": "hi how are you",
  "response": "I'm doing well, thanks for asking!",
  "conversation_token_estimate": 45
}
```

## Supported Casual Chat Examples

- Greetings: "hi", "hello", "hey"
- Personal questions: "how are you", "who are you", "what's your name"
- General info: "what time is it", "where do you stay", "what's your gender", "who is your boss"
- Any non-database, non-sarcastic conversational query

## Testing

To test the casual chat intent:

```bash
POST /database/test-intent
{
  "question": "hi how are you"
}
```

Expected response:
```json
{
  "question": "hi how are you",
  "detected_intent": "casual_chat",
  "description": "Casual conversation - Web search",
  "conversation_context_used": false,
  "messages_in_memory": 0
}
```
