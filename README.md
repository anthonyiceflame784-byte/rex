"""
README - REX AI System Documentation
"""

# REX - Reasoning Engine eXtended

A modular, production-ready JARVIS-style AI system with advanced capabilities for autonomous reasoning, learning, and expansion.

## 🚀 Features

### Core Architecture
- **Advanced Reasoning Engine** - Multi-path reasoning (Logical, Creative, Analytical, Heuristic, Probabilistic)
- **Intelligent Memory System** - Dual-layer memory (short-term & long-term with encryption)
- **Natural Language Processing** - Intent detection, entity extraction, semantic analysis
- **Permission-Based Security** - Role-based access control with audit logging
- **Multi-Agent System** - Autonomous agents with task coordination
- **Plugin Architecture** - Sandboxed extensible plugin system
- **Voice Interface** - Speech-to-text and text-to-speech integration
- **REST API** - Full HTTP API for external integration
- **Self-Expansion** - Autonomous code generation and learning

### Security & Reliability
✅ Permission system for all sensitive operations
✅ Audit logging for compliance
✅ Code validation and sandboxing
✅ Error handling and recovery
✅ Graceful shutdown

### Advanced Features
✅ Multi-path reasoning with confidence scoring
✅ Context-aware memory retrieval
✅ Autonomous agent coordination
✅ Plugin hot-loading
✅ Voice command support
✅ RESTful API with comprehensive endpoints
✅ Self-learning capabilities
✅ Code generation with safety validation

## 📁 Project Structure

```
rex/
├── main.py                 # Main entry point
├── config/
│   └── settings.py        # System configuration
├── core/
│   ├── engine.py          # Main AI engine
│   ├── memory.py          # Memory system
│   ├── reasoning.py       # Reasoning engine
│   └── nlp.py             # NLP module
├── security/
│   └── permission_system.py  # Permission management
├── agents/
│   └── manager.py         # Agent coordination
├── plugins/
│   └── manager.py         # Plugin system
├── voice/
│   └── interface.py       # Voice I/O
├── api/
│   └── server.py          # REST API
├── self_expansion/
│   └── system.py          # Self-expansion module
├── utils/
│   └── logger.py          # Logging utility
└── logs/                  # Log files
```

## 🏃 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/anthonyiceflame784-byte/rex.git
cd rex

# Install dependencies
pip install -r requirements.txt
```

### Running REX

```bash
# Interactive mode
python main.py

# The system will display:
# ╔════════════════════════════════════════╗
# ║     REX - Reasoning Engine eXtended    ║
# ║          AI System v1.0                ║
# ╚════════════════════════════════════════╝
```

### Example Interactions

```
You: What is artificial intelligence?
REX: Based on question analysis: 
AI is the field of computer science...
[Confidence: 85%]

You: Execute the backup protocol
REX: Based on command analysis:
Backup protocol initiated...
[Confidence: 90%]

You: status
REX: [System status displayed]

You: exit
REX: REX shutting down. Goodbye.
```

## 🔧 Core Components

### 1. AI Engine (`core/engine.py`)
Orchestrates all systems:
- Query processing pipeline
- Intent detection
- Reasoning execution
- Memory integration
- Response generation

**Usage:**
```python
from core.engine import AIEngine
from security.permission_system import PermissionManager

pm = PermissionManager()
engine = AIEngine(pm)
engine.initialize()
response = engine.process("Your query here")
```

### 2. Memory System (`core/memory.py`)
Dual-layer memory with persistence:
- **Short-term**: Fast, limited capacity (1000 items)
- **Long-term**: Persistent SQLite storage (10000 items)

**Usage:**
```python
from core.memory import MemorySystem

memory = MemorySystem()
memory.remember("Important fact", persist=True)
results = memory.recall("search query")
```

### 3. Reasoning Engine (`core/reasoning.py`)
Multiple reasoning paths:
- Logical deduction
- Creative exploration
- Analytical breakdown
- Heuristic reasoning
- Probabilistic analysis

**Usage:**
```python
from core.reasoning import ReasoningEngine, ReasoningPath

reasoning = ReasoningEngine()
conclusion, confidence = reasoning.reason(
    "Your question",
    preferred_paths=[ReasoningPath.LOGICAL]
)
```

### 4. NLP Engine (`core/nlp.py`)
Natural language understanding:
- Intent extraction
- Entity recognition
- Keyword analysis
- Query type detection

**Usage:**
```python
from core.nlp import NLPEngine

nlp = NLPEngine()
parsed = nlp.parse_query("What is the weather?")
print(parsed.intent, parsed.entities)
```

### 5. Agent System (`agents/manager.py`)
Autonomous agent coordination:
- AnalysisAgent - Data processing
- ExecutionAgent - Command execution
- LearningAgent - Knowledge acquisition

**Usage:**
```python
from agents.manager import AgentManager, AgentTask

manager = AgentManager()
task = AgentTask(
    task_id="task_001",
    name="Analyze Data",
    target_agent="agent_analysis_001",
    parameters={"data": [1, 2, 3]}
)
result = manager.assign_task("agent_analysis_001", task)
```

### 6. Plugin System (`plugins/manager.py`)
Extensible plugin architecture:
- Analysis Plugin
- API Integration Plugin
- Automation Plugin
- Custom plugins

**Usage:**
```python
from plugins.manager import PluginManager

plugin_mgr = PluginManager()
plugin_mgr.load_builtin_plugins()
result = plugin_mgr.execute_plugin("Analysis", "analyze", {"data": [1,2,3]})
```

### 7. Voice Interface (`voice/interface.py`)
Speech recognition and synthesis:
- Google TTS/STT
- Azure TTS/STT
- Customizable languages and speeds

**Usage:**
```python
from voice.interface import VoiceInterface, VoiceEngine

voice = VoiceInterface(
    tts_engine=VoiceEngine.GOOGLE,
    stt_engine=VoiceEngine.GOOGLE
)
voice.speak("Hello, I am REX")
text = voice.listen()
```

### 8. REST API (`api/server.py`)
HTTP endpoints:
- Query processing: `POST /query`
- Memory operations: `GET/POST /memory`
- Agent status: `GET /agents`
- Plugin control: `GET/POST /plugins`
- System health: `GET /health`

### 9. Self-Expansion (`self_expansion/system.py`)
Autonomous code generation:
- Template-based code generation
- Code validation and safety checks
- Learning from interactions
- Module generation and review

**Usage:**
```python
from self_expansion.system import SelfExpansionSystem

expansion = SelfExpansionSystem()
result = expansion.generate_module(
    "my_module",
    "Create a function that processes data"
)
```

### 10. Security System (`security/permission_system.py`)
Permission-based access control:
- Action-level permissions
- Audit logging
- User approval workflows

**Usage:**
```python
from security.permission_system import request_permission

if request_permission("core_modification", "Modify core logic"):
    # Safe operation
    pass
else:
    print("Permission denied")
```

## ⚙️ Configuration

Edit `config/settings.py`:

```python
# System config
SYSTEM_CONFIG = {
    "name": "REX",
    "version": "1.0.0",
    "max_memory_mb": 2048,
    "max_agents": 10,
}

# Memory config
MEMORY_CONFIG = {
    "max_short_term_items": 1000,
    "max_long_term_items": 10000,
    "enable_encryption": True,
}

# Security config
SECURITY_CONFIG = {
    "require_permissions": True,
    "permission_level": "strict",
    "enable_audit_log": True,
}

# API config
API_CONFIG = {
    "enable_rest_api": True,
    "api_port": 5000,
    "api_host": "127.0.0.1",
}
```

## 🔐 Permission System

All sensitive operations require permission:

```python
from security.permission_system import request_permission

# Request permission for an action
if request_permission("agent_spawn", "Spawn new analysis agent"):
    # Action approved
    pass
else:
    # Action denied
    pass
```

Permission levels:
- **DENY** - Always rejected
- **USER_APPROVAL** - Requires user confirmation
- **RESTRICTED** - Requires review
- **ALLOWED** - Always approved

## 📊 System Status

Get system status:

```bash
You: status

REX: 
╔════════════════════════════════════╗
║        REX System Status           ║
╚════════════════════════════════════╝

Status: RUNNING
Uptime: 3600s
Queries Processed: 42
Last Activity: 2026-06-03 09:00:00

Memory Status:
- Short-term items: 15
- Memory initialized: Yes

Components: All Operational
```

## 🚀 Commands

Available commands in interactive mode:

```
help              - Show help message
status            - Show system status
exit              - Shutdown REX
```

Plus any natural language query!

## 📝 Logging

All activities logged to `logs/rex.log`:

```
2026-06-03 09:00:00 - core.engine - INFO - AIEngine initialized
2026-06-03 09:00:15 - core.engine - INFO - Query 1: Intent=information_retrieval
```

Set log level in `config/settings.py`:
- DEBUG - Detailed debugging
- INFO - General information
- WARNING - Warnings
- ERROR - Errors
- CRITICAL - Critical errors

## 🔧 Extending REX

### Creating Custom Agents

```python
from agents.manager import Agent

class MyAgent(Agent):
    def __init__(self):
        super().__init__(
            agent_id="agent_custom_001",
            name="My Agent",
            description="Custom agent",
            capabilities=["custom_task"]
        )
    
    def _execute(self, task):
        return "Task result"

# Register
manager.register_agent(MyAgent())
```

### Creating Custom Plugins

```python
from plugins.manager import Plugin, PluginMetadata

class MyPlugin(Plugin):
    def __init__(self):
        metadata = PluginMetadata(
            name="MyPlugin",
            version="1.0.0",
            author="You",
            description="Custom plugin",
            capabilities=["custom_capability"]
        )
        super().__init__(metadata)
    
    def initialize(self):
        return True
    
    def execute(self, command, args=None):
        return "Result"

# Register
plugin_mgr.register_plugin(MyPlugin())
```

## 🐛 Troubleshooting

### Engine won't start
- Check `logs/rex.log` for errors
- Ensure all dependencies installed
- Verify `config/settings.py` syntax

### Permission denied
- Check permission levels in `security/permission_system.py`
- Review audit log in `logs/audit.log`
- Adjust permissions in `config/settings.py`

### Memory issues
- Clear short-term memory: `You: clear_memory`
- Check memory config in `config/settings.py`
- Run cleanup: `engine.execute_command("cleanup")`

## 📈 Performance

- Query processing: ~100-500ms
- Memory recall: ~10-50ms
- Reasoning execution: ~200-1000ms
- Agent task execution: ~50-200ms

## 🔄 Future Enhancements

- [ ] Multi-user support
- [ ] Distributed agents
- [ ] Advanced NLP (transformers)
- [ ] Reinforcement learning
- [ ] Advanced visualization
- [ ] Real-time collaboration
- [ ] Cloud integration

## 📄 License

MIT License - See LICENSE file

## 👤 Author

Created by anthonyiceflame784-byte

## 🤝 Contributing

Contributions welcome! Please ensure:
- All code follows project architecture
- Maintain security standards
- Add comprehensive docstrings
- Include error handling
- Pass validation

## 📧 Support

For issues and questions, open a GitHub issue.

---

**REX v1.0.0** - Your Advanced AI System
