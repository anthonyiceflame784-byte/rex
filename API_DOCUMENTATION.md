"""
API Documentation for REX AI System.
"""

# REX AI System - API Documentation

## Overview

The REX API provides comprehensive HTTP endpoints for interacting with the AI system. All endpoints follow REST conventions and return standardized JSON responses.

## Base URL

```
http://localhost:5000
```

## Response Format

All API responses follow this standard format:

```json
{
  "success": true,
  "status_code": 200,
  "timestamp": "2026-06-03T09:00:00.000000",
  "data": {},
  "message": "Success message",
  "error": ""
}
```

## Authentication

Currently, no authentication is required. Future versions will support:
- API keys
- OAuth 2.0
- JWT tokens

## Query Endpoints

### POST /api/query
Process a query through the AI engine.

**Request:**
```json
{
  "query": "What is artificial intelligence?"
}
```

**Response:**
```json
{
  "success": true,
  "status_code": 200,
  "data": {
    "response": "Based on question analysis: AI is the field..."
  },
  "message": "Query processed successfully"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is AI?"}'
```

## Memory Endpoints

### GET /api/memory/recall
Recall memories based on query.

**Parameters:**
- `q` (required): Search query

**Response:**
```json
{
  "success": true,
  "data": {
    "query": "test",
    "results": [
      {
        "content": "Memory content",
        "type": "fact",
        "importance": 0.85,
        "tags": ["test", "memory"]
      }
    ],
    "count": 1
  }
}
```

**Example:**
```bash
curl http://localhost:5000/api/memory/recall?q=test
```

### POST /api/memory/store
Store a new memory item.

**Request:**
```json
{
  "content": "Important fact to remember",
  "type": "fact",
  "importance": 0.8,
  "tags": ["important", "reference"]
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "stored": true
  },
  "message": "Memory stored successfully"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/memory/store \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Python is a programming language",
    "type": "fact"
  }'
```

### POST /api/memory/clear
Clear short-term memory.

**Response:**
```json
{
  "success": true,
  "data": {
    "cleared": true
  },
  "message": "Memory cleared successfully"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/memory/clear
```

## Reasoning Endpoints

### GET /api/reasoning/trace
Get the current reasoning trace.

**Response:**
```json
{
  "success": true,
  "data": {
    "steps": 3,
    "paths_used": ["logical", "analytical"],
    "avg_confidence": 0.83,
    "trace": "Step 1 [logical]: Applying logical deduction..."
  }
}
```

**Example:**
```bash
curl http://localhost:5000/api/reasoning/trace
```

## Agent Endpoints

### GET /api/agents/status
Get status of all agents.

**Response:**
```json
{
  "success": true,
  "data": {
    "agents": {
      "agent_analysis_001": {
        "id": "agent_analysis_001",
        "name": "Analysis Agent",
        "state": "idle",
        "capabilities": ["data_analysis", "pattern_detection"],
        "tasks_completed": 5,
        "current_task": null
      }
    },
    "total": 3
  }
}
```

**Example:**
```bash
curl http://localhost:5000/api/agents/status
```

### GET /api/agents/{agent_id}/status
Get status of specific agent.

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "agent_analysis_001",
    "name": "Analysis Agent",
    "state": "idle",
    "capabilities": ["data_analysis"],
    "tasks_completed": 5,
    "current_task": null
  }
}
```

**Example:**
```bash
curl http://localhost:5000/api/agents/agent_analysis_001/status
```

## Plugin Endpoints

### GET /api/plugins/status
Get status of all plugins.

**Response:**
```json
{
  "success": true,
  "data": {
    "plugins": {
      "Analysis": {
        "name": "Analysis",
        "version": "1.0.0",
        "enabled": true,
        "initialized": true,
        "capabilities": ["analyze", "statistics", "visualization"]
      }
    },
    "total": 3
  }
}
```

**Example:**
```bash
curl http://localhost:5000/api/plugins/status
```

### POST /api/plugins/execute
Execute a plugin command.

**Request:**
```json
{
  "plugin": "Analysis",
  "command": "analyze",
  "args": {
    "data": [1, 2, 3, 4, 5]
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "result": "Analysis complete: 5 data points processed"
  },
  "message": "Plugin command executed"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/plugins/execute \
  -H "Content-Type: application/json" \
  -d '{
    "plugin": "Analysis",
    "command": "analyze",
    "args": {"data": [1,2,3]}
  }'
```

### POST /api/plugins/{plugin_name}/enable
Enable a plugin.

**Response:**
```json
{
  "success": true,
  "data": {
    "enabled": true
  },
  "message": "Plugin enabled: Analysis"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/plugins/Analysis/enable
```

### POST /api/plugins/{plugin_name}/disable
Disable a plugin.

**Response:**
```json
{
  "success": true,
  "data": {
    "disabled": true
  },
  "message": "Plugin disabled: Analysis"
}
```

**Example:**
```bash
curl -X POST http://localhost:5000/api/plugins/Analysis/disable
```

## System Endpoints

### GET /api/system/status
Get overall system status.

**Response:**
```json
{
  "success": true,
  "data": {
    "running": true,
    "uptime_seconds": 3600,
    "requests_served": 42,
    "engine_status": ["Status: RUNNING", "Uptime: 3600s"]
  },
  "message": "System status retrieved"
}
```

**Example:**
```bash
curl http://localhost:5000/api/system/status
```

### GET /api/health
Health check endpoint.

**Response:**
```json
{
  "success": true,
  "status_code": 200,
  "data": {
    "status": "healthy",
    "running": true
  },
  "message": "System is operational"
}
```

**Example:**
```bash
curl http://localhost:5000/api/health
```

## Error Responses

### 400 Bad Request
```json
{
  "success": false,
  "status_code": 400,
  "error": "Invalid request parameters",
  "message": "Query parameter is required"
}
```

### 404 Not Found
```json
{
  "success": false,
  "status_code": 404,
  "error": "Resource not found",
  "message": "Plugin 'NonExistent' not found"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "status_code": 500,
  "error": "Internal server error",
  "message": "An unexpected error occurred"
}
```

## Using the Python Client

### Installation

```python
from api.client import REXAPIClient

client = REXAPIClient(base_url="http://localhost:5000")
```

### Query

```python
response = client.query("What is machine learning?")
print(response["data"]["response"])
```

### Memory Operations

```python
# Store memory
client.store_memory("Python is great", "fact")

# Recall memory
results = client.recall_memory("Python")
for item in results["data"]["results"]:
    print(item["content"])

# Clear memory
client.clear_memory()
```

### Agents

```python
# Get all agents status
agents = client.get_agents_status()
print(agents["data"]["agents"])

# Get specific agent
agent = client.get_agent_status("agent_analysis_001")
print(agent["data"])
```

### Plugins

```python
# Get all plugins
plugins = client.get_plugins_status()
print(plugins["data"]["plugins"])

# Execute plugin
result = client.execute_plugin(
    "Analysis", 
    "analyze", 
    {"data": [1, 2, 3]}
)
print(result["data"]["result"])

# Enable/disable plugin
client.enable_plugin("Analysis")
client.disable_plugin("Analysis")
```

### System

```python
# Get system status
status = client.system_status()
print(f"Uptime: {status['data']['uptime_seconds']}s")

# Check health
health = client.health_check()
print(f"Healthy: {health['data']['status']}")
```

## Rate Limiting

Currently, no rate limiting is implemented. Future versions will include:
- Per-IP rate limits
- Per-API-key rate limits
- Burst allowances
- Throttling policies

## Webhooks

Future implementation will support:
- Event subscriptions
- Webhook delivery
- Retry mechanisms
- Signature verification

## Versioning

Current API version: **v1.0**

Future versions will use header-based versioning:
```
Accept: application/vnd.rex.v2+json
```

## CORS

CORS is enabled by default for development. Configuration available in `config/settings.py`.

## Timeouts

- Default request timeout: 30 seconds
- Long operations timeout: 60 seconds
- Can be configured via client

## Pagination

Future endpoints will support pagination:
```
GET /api/memory/recall?q=test&page=1&limit=20
```

## Filtering

Future endpoints will support advanced filtering:
```
GET /api/memory/recall?q=test&type=fact&min_importance=0.7
```

## Examples

### Complete Query Example

```python
from api.client import REXAPIClient
import json

client = REXAPIClient()

# Process query
response = client.query("How does machine learning work?")

if response["success"]:
    print("Response:", response["data"]["response"])
    print("Confidence:", response["data"]["confidence"])
else:
    print("Error:", response["error"])

# Get reasoning trace
trace = client.get_reasoning_trace()
print("Reasoning Trace:", trace["data"]["trace"])

# Store result
client.store_memory(
    f"Q: How does machine learning work?\nA: {response['data']['response']}",
    "interaction"
)

client.close()
```

### Agent Task Example

```python
from api.client import REXAPIClient

client = REXAPIClient()

# Get agents
agents = client.get_agents_status()
print("Available agents:", list(agents["data"]["agents"].keys()))

# Get specific agent
agent_status = client.get_agent_status("agent_analysis_001")
print(f"Agent {agent_status['data']['name']} is {agent_status['data']['state']}")

client.close()
```

### Plugin Usage Example

```python
from api.client import REXAPIClient
import json

client = REXAPIClient()

# List all plugins
plugins = client.get_plugins_status()
print("Available plugins:")
for name, info in plugins["data"]["plugins"].items():
    print(f"  - {name}: {', '.join(info['capabilities'])}")

# Execute analysis plugin
result = client.execute_plugin(
    "Analysis",
    "analyze",
    {"data": [10, 20, 30, 40, 50]}
)
print("Analysis result:", result["data"]["result"])

client.close()
```

## Testing API

### Using cURL

```bash
# Test health
curl http://localhost:5000/api/health

# Test query
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "Hello"}'

# Test memory
curl -X POST http://localhost:5000/api/memory/store \
  -H "Content-Type: application/json" \
  -d '{"content": "Test", "type": "fact"}'
```

### Using Postman

1. Import collection from `api/postman_collection.json`
2. Set base URL to `http://localhost:5000`
3. Run requests

### Using Python

```python
import requests

url = "http://localhost:5000/api/query"
data = {"query": "What is AI?"}

response = requests.post(url, json=data)
print(response.json())
```

## Troubleshooting

### Connection Refused
- Ensure REX server is running: `python main.py`
- Check if port 5000 is available
- Verify firewall settings

### Response Timeout
- Increase client timeout
- Check server logs for errors
- Reduce query complexity

### Plugin Not Found
- Check plugin is enabled
- Verify plugin name spelling
- List available plugins via `/api/plugins/status`

### Memory Issues
- Clear memory: `/api/memory/clear`
- Check memory usage
- Optimize memory settings in config

---

**REX API Documentation v1.0** - Last Updated: 2026-06-03
