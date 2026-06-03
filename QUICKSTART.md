"""
Quick Start Guide for REX AI System.
"""

# REX Quick Start Guide

Get up and running with REX in minutes!

## Prerequisites

- Python 3.10+
- pip (Python package manager)
- Git (optional)

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/anthonyiceflame784-byte/rex.git
cd rex
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running REX

### Interactive Mode

```bash
python main.py
```

This starts REX in interactive mode with a CLI interface:

```
╔════════════════════════════════════════╗
║     REX - Reasoning Engine eXtended    ║
║          AI System v1.0                ║
╚════════════════════════════════════════╝

System initialized at 2026-06-03 09:00:00
Type 'help' for commands, 'exit' to quit

You: 
```

### Basic Commands

```bash
You: help              # Show available commands
You: status            # Show system status
You: exit              # Shutdown REX
```

### Example Interactions

```bash
You: What is artificial intelligence?

REX: Based on question analysis:
AI is the field of computer science that focuses on...
[Confidence: 85%]

---

You: Tell me about Python programming

REX: Based on question analysis:
Python is a high-level programming language...
[Confidence: 80%]

---

You: status

REX: 
╔════════════════════════════════════╗
║        REX System Status           ║
╚════════════════════════════════════╝

Status: RUNNING
Uptime: 120s
Queries Processed: 3
```

## Using the REST API

### Start API Server

```bash
# REX starts API automatically on port 5000
python main.py
```

### Basic API Calls

#### Check Health

```bash
curl http://localhost:5000/api/health
```

Response:
```json
{
  "success": true,
  "data": {"status": "healthy", "running": true}
}
```

#### Send Query

```bash
curl -X POST http://localhost:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is machine learning?"}'
```

#### Store Memory

```bash
curl -X POST http://localhost:5000/api/memory/store \
  -H "Content-Type: application/json" \
  -d '{"content": "Python is great", "type": "fact"}'
```

#### Get System Status

```bash
curl http://localhost:5000/api/system/status
```

## Using Python Client

```python
from api.client import REXAPIClient

# Initialize client
client = REXAPIClient()

# Send query
response = client.query("What is AI?")
print(response["data"]["response"])

# Store memory
client.store_memory("Important fact", "fact")

# Get system status
status = client.system_status()
print(f"Uptime: {status['data']['uptime_seconds']}s")

client.close()
```

## Docker Deployment

### Build Image

```bash
docker build -t rex:latest .
```

### Run Container

```bash
docker run -p 5000:5000 rex:latest
```

### Using Docker Compose

```bash
docker-compose up -d
docker-compose logs -f
```

## Configuration

Edit `config/settings.py` to customize:

```python
# Log level
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR, CRITICAL

# Memory settings
MEMORY_CONFIG = {
    "max_short_term_items": 1000,
    "max_long_term_items": 10000,
}

# Security
SECURITY_CONFIG = {
    "require_permissions": True,
    "enable_audit_log": True,
}

# API
API_CONFIG = {
    "api_port": 5000,
    "api_host": "127.0.0.1",
}
```

## Project Structure

```
rex/
├── main.py                 # Entry point
├── core/
│   ├── engine.py          # Main AI engine
│   ├── memory.py          # Memory system
│   ├── reasoning.py       # Reasoning engine
│   └── nlp.py             # NLP module
├── agents/                # Autonomous agents
├── plugins/               # Plugin system
├── voice/                 # Voice interface
├── api/                   # REST API
├── security/              # Permission system
├── config/                # Configuration
├── logs/                  # Log files
└── README.md              # Full documentation
```

## Features Overview

### Core Capabilities

✅ **Natural Language Processing** - Understand user intent
✅ **Multi-Path Reasoning** - Logical, creative, analytical
✅ **Dual-Layer Memory** - Short-term & long-term storage
✅ **Autonomous Agents** - Task execution & coordination
✅ **Plugin System** - Extensible architecture
✅ **Voice Interface** - Speech recognition & synthesis
✅ **REST API** - HTTP endpoints
✅ **Self-Expansion** - Code generation & learning
✅ **Security** - Permission-based access control

### Built-In Plugins

- **Analysis Plugin** - Data analysis and statistics
- **API Integration** - External API calls
- **Automation** - Task scheduling and workflows

### Built-In Agents

- **Analysis Agent** - Process and analyze data
- **Execution Agent** - Execute commands and tasks
- **Learning Agent** - Learn from interactions

## Testing

Run the test suite:

```bash
pytest tests/
```

Run specific test:

```bash
pytest tests/test_rex.py::TestMemorySystem -v
```

## Troubleshooting

### REX won't start

Check logs:
```bash
tail -f logs/rex.log
```

Verify dependencies:
```bash
pip list | grep -E "python-dotenv|pydantic|flask"
```

### API connection refused

Ensure REX is running:
```bash
curl http://localhost:5000/api/health
```

Check firewall settings and port availability:
```bash
# Windows
netstat -ano | findstr :5000

# Linux/Mac
lsof -i :5000
```

### Memory issues

Clear short-term memory:
```bash
You: clear_memory
```

Check configuration limits in `config/settings.py`.

## Next Steps

1. **Explore Features**
   - Try different queries
   - Use voice interface
   - Test plugins

2. **Extend REX**
   - Create custom agents
   - Build plugins
   - Add API endpoints

3. **Deploy**
   - Use Docker
   - Set up monitoring
   - Configure production settings

4. **Integrate**
   - Connect to external services
   - Build custom frontends
   - Add authentication

## Learning Resources

### Documentation
- **README.md** - Full feature documentation
- **ARCHITECTURE.md** - System design
- **API_DOCUMENTATION.md** - API reference
- **DEVELOPMENT.md** - Development guide

### Example Code

Check the `tests/` directory for usage examples of all components.

### External Resources

- [Python Documentation](https://docs.python.org/3/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## Common Tasks

### Add Custom Agent

```python
from agents.manager import Agent

class MyAgent(Agent):
    def __init__(self):
        super().__init__(
            agent_id="agent_custom_001",
            name="My Agent",
            description="Custom agent",
            capabilities=["my_capability"]
        )
    
    def _execute(self, task):
        return "Task result"
```

### Create Plugin

```python
from plugins.manager import Plugin, PluginMetadata

class MyPlugin(Plugin):
    def __init__(self):
        metadata = PluginMetadata(
            name="MyPlugin",
            version="1.0.0",
            author="You",
            description="Custom plugin",
            capabilities=["my_capability"]
        )
        super().__init__(metadata)
    
    def initialize(self):
        return True
    
    def execute(self, command, args=None):
        return f"Executed: {command}"
```

### Query Memory

```python
# Via API
curl "http://localhost:5000/api/memory/recall?q=important"

# Via Python
from api.client import REXAPIClient
client = REXAPIClient()
results = client.recall_memory("important")
```

## Performance Tips

1. **Optimize Queries** - Be specific in queries
2. **Clear Memory** - Use `clear_memory` command periodically
3. **Monitor Logs** - Check logs for errors and bottlenecks
4. **Adjust Config** - Tune memory settings for your use case
5. **Use Agents** - Distribute workload across agents

## Security Best Practices

1. **Enable Permissions** - Keep `require_permissions: True`
2. **Monitor Audit Log** - Check `logs/audit.log` regularly
3. **Validate Input** - Validate user input before processing
4. **Update Dependencies** - Keep packages updated
5. **Use HTTPS** - In production, use HTTPS for API

## Getting Help

1. **Check Documentation** - See README, ARCHITECTURE, API_DOCUMENTATION
2. **Review Logs** - Check `logs/rex.log` for errors
3. **Test Components** - Run tests with `pytest tests/`
4. **Open Issue** - Create GitHub issue with details

## Feedback & Contributions

We welcome feedback and contributions! Please:
1. Check existing issues
2. Provide detailed description
3. Include logs and error messages
4. Submit pull requests with tests

---

**Welcome to REX!** 🚀

Start your journey with:
```bash
python main.py
```

For full documentation, see:
- **README.md** - Feature overview
- **ARCHITECTURE.md** - System design
- **API_DOCUMENTATION.md** - API details
- **DEVELOPMENT.md** - Development guide
