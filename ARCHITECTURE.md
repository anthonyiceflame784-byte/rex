"""
Architecture documentation for REX AI System.
"""

# REX Architecture

## System Overview

REX (Reasoning Engine eXtended) is a modular AI system designed with the following principles:

1. **Modularity** - Independent, interchangeable components
2. **Extensibility** - Easy to add new features and capabilities
3. **Security** - Permission-based access control throughout
4. **Reliability** - Error handling, logging, graceful shutdown
5. **Performance** - Optimized for responsive interaction
6. **Scalability** - Designed to grow with features and agents

## Architectural Layers

```
┌─────────────────────────────────────────┐
│         User Interface Layer            │
│  (CLI, Voice, API, GUI)                 │
└─────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│       Integration Layer                 │
│  (API Server, Voice Interface)          │
└─────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│       Application Logic Layer           │
│  (AI Engine, Agents, Plugins)           │
└─────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│        Core Processing Layer            │
│  (Reasoning, NLP, Memory)               │
└─────────────────────────────────────────┘
                  ▼
┌─────────────────────────────────────────┐
│        Security & Storage Layer         │
│  (Permissions, Database, Encryption)    │
└─────────────────────────────────────────┘
```

## Component Architecture

### Core Components

```
┌──────────────────────────────────────────────────┐
│                  AI Engine                       │
│  (Orchestrates all systems)                      │
└──────────────────────────────────────────────────┘
       │         │          │         │
       ▼         ▼          ▼         ▼
    ┌────┐  ┌────────┐  ┌────┐  ┌────────┐
    │NLP │  │Reasoning│ │Memory  │Voice
    └────┘  └────────┘  └────┘  └────────┘
```

### System Components

```
┌──────────────────────────────────────────────────┐
│                 AI Engine                        │
└──────────────────────────────────────────────────┘
       │           │          │          │
       ▼           ▼          ▼          ▼
  ┌────────┐  ┌────────┐  ┌────────┐  ┌──────┐
  │ Agents │  │ Plugins│  │ Self   │  │ API  │
  │        │  │        │  │ Expand │  │Server│
  └────────┘  └────────┘  └────────┘  └──────┘
```

### Security Layer

```
All Components
     │
     ▼
┌──────────────────────────────────────┐
│  Permission System                   │
│  - Check permissions                 │
│  - Audit logging                     │
│  - Policy enforcement                │
└──────────────────────────────────────┘
```

## Data Flow

### Query Processing Pipeline

```
User Input
   │
   ▼
┌─────────────────┐
│  NLP Engine     │  ← Parse intent, extract entities
└─────────────────┘
   │
   ▼
┌─────────────────┐
│ Memory Recall   │  ← Retrieve relevant context
└─────────────────┘
   │
   ▼
┌─────────────────┐
│ Reasoning       │  ← Multi-path reasoning
│ Engine          │
└─────────────────┘
   │
   ▼
┌─────────────────┐
│ Response        │  ← Generate natural language response
│ Generator       │
└─────────────────┘
   │
   ▼
┌─────────────────┐
│ Memory Store    │  ← Save interaction
└─────────────────┘
   │
   ▼
User Output
```

### Agent Task Execution

```
Task Request
   │
   ▼
┌──────────────────┐
│ Agent Manager    │  ← Find suitable agent
└──────────────────┘
   │
   ▼
┌──────────────────┐
│ Permission Check │  ← Verify allowed
└──────────────────┘
   │
   ▼
┌──────────────────┐
│ Agent Execution  │  ← Execute task
└──────────────────┘
   │
   ▼
┌──────────────────┐
│ Result Storage   │  ← Log results
└──────────────────┘
```

## Module Dependencies

```
main.py
  │
  ├─ core/engine.py
  │    ├─ core/memory.py
  │    ├─ core/reasoning.py
  │    ├─ core/nlp.py
  │    ├─ agents/manager.py
  │    ├─ plugins/manager.py
  │    └─ security/permission_system.py
  │
  ├─ api/server.py
  │    └─ (depends on engine)
  │
  ├─ voice/interface.py
  │    └─ (independent)
  │
  └─ self_expansion/system.py
       └─ security/permission_system.py
```

## Permission Model

### Permission Levels

```
┌──────────────────────────────────┐
│      Permission Request          │
└──────────────────────────────────┘
       │
       ▼
┌──────────────────────────────────┐
│   Check Permission Level         │
└──────────────────────────────────┘
       │
   ┌───┼───┬───────────┬──────────┐
   │   │   │           │          │
   ▼   ▼   ▼           ▼          ▼
 DENY USER RESTRICTED ALLOWED  (default)
      APPROVAL
```

### Protected Operations

```
Core Modifications     → DENY
Memory Write          → RESTRICTED
Plugin Installation   → USER_APPROVAL
Agent Spawning        → RESTRICTED
System Shutdown       → USER_APPROVAL
Code Generation       → RESTRICTED
Self Modification     → DENY
External API Calls    → ALLOWED
File System Access    → RESTRICTED
Network Access        → ALLOWED
```

## Memory Architecture

### Dual-Layer Memory System

```
┌────────────────────────────────────────┐
│      Short-Term Memory                 │
│  - In-memory storage (RAM)            │
│  - Max 1000 items                     │
│  - Fast retrieval                     │
│  - Volatile (cleared on shutdown)     │
└────────────────────────────────────────┘

┌────────────────────────────────────────┐
│      Long-Term Memory                  │
│  - SQLite persistent storage          │
│  - Max 10000 items                    │
│  - Encrypted storage option           │
│  - 365-day retention                  │
└────────────────────────────────────────┘
```

### Memory Types

- **fact** - Learned information
- **conversation** - User interactions
- **learning** - Knowledge acquired
- **event** - System events
- **interaction** - Query/response pairs

## Reasoning Paths

```
┌─────────────────────────────────────────┐
│    Query Input                          │
└─────────────────────────────────────────┘
   │
   ├─ Logical Path         ─→ Deduction, inference
   │
   ├─ Creative Path        ─→ Novel ideas, lateral thinking
   │
   ├─ Analytical Path      ─→ Component breakdown
   │
   ├─ Heuristic Path       ─→ Experience-based rules
   │
   └─ Probabilistic Path   ─→ Statistics, likelihood

   │
   ▼
┌─────────────────────────────────────────┐
│    Combine Results                      │
│    - Average confidence                │
│    - Merge conclusions                 │
│    - Select best answer                │
└─────────────────────────────────────────┘
```

## Agent Coordination Model

```
┌──────────────────────┐
│   Agent Manager      │
│  (Central Registry)  │
└──────────────────────┘
    │    │    │
    ▼    ▼    ▼
┌───────────────────────────────────┐
│  Agent 1    │  Agent 2  │  Agent 3│
│  (Analysis) │  (Execute)│ (Learn) │
└───────────────────────────────────┘
    │    │    │
    └────┴────┴─ Message Queue
```

## Plugin Architecture

```
┌──────────────────────┐
│  Plugin Manager      │
│  (Central Registry)  │
└──────────────────────┘
    │    │    │
    ▼    ▼    ▼
┌────────────────────────────────────────┐
│  Plugin 1     │  Plugin 2  │  Plugin 3 │
│  (Analysis)   │  (API)     │  (Auto)   │
│  [Sandboxed]  │[Sandboxed] │[Sandboxed]│
└────────────────────────────────────────┘
    │    │    │
    └────┴────┴─ Hook System
```

## Self-Expansion Architecture

```
┌─────────────────────────────────────┐
│  Expansion Request                  │
└─────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────┐
│  Code Generator                     │
│  - Template selection               │
│  - Code generation                  │
└─────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────┐
│  Validator                          │
│  - Syntax check                     │
│  - Security validation              │
│  - Pattern detection                │
└─────────────────────────────────────┘
   │
   ├─ Valid ─→ Code Generated ✓
   │
   └─ Invalid ─→ Error ✗

   │
   ▼
┌─────────────────────────────────────┐
│  Learning System                    │
│  - Pattern recording                │
│  - Experience update                │
└─────────────────────────────────────┘
```

## API Architecture

```
┌────────────────────────────────────┐
│      HTTP Request                  │
└────────────────────────────────────┘
   │
   ▼
┌────────────────────────────────────┐
│   API Server Router                │
│   - Path matching                  │
│   - Method validation              │
└────────────────────────────────────┘
   │
   ├─ /query           → AI Engine
   ├─ /memory/*        → Memory System
   ├─ /agents/*        → Agent Manager
   ├─ /plugins/*       → Plugin Manager
   ├─ /reasoning/*     → Reasoning Engine
   └─ /system/*        → System Info

   │
   ▼
┌────────────────────────────────────┐
│      Process Request               │
└────────────────────────────────────┘
   │
   ▼
┌────────────────────────────────────┐
│   Standardized Response            │
│   {                                │
│     "success": bool,               │
│     "data": {...},                 │
│     "message": str,                │
│     "error": str                   │
│   }                                │
└────────────────────────────────────┘
```

## Deployment Architecture

### Local Deployment
```
┌─────────────────┐
│   REX Server    │
│   (main.py)     │
│   - Interactive │
│   - CLI mode    │
│   - API port    │
└─────────────────┘
```

### Docker Deployment
```
┌──────────────────────────────────┐
│   Docker Container               │
│  ┌─────────────────────────────┐ │
│  │  REX AI System              │ │
│  │  - Python 3.10              │ │
│  │  - All dependencies         │ │
│  │  - Port 5000 exposed        │ │
│  └─────────────────────────────┘ │
└──────────────────────────────────┘
```

### Compose Deployment
```
┌─────────────────────────────────────┐
│      Docker Compose Network         │
├─────────────────────────────────────┤
│  ┌────────┐  ┌──────┐  ┌────────┐  │
│  │  REX   │  │  DB  │  │ Cache  │  │
│  │  API   │  │ (PG) │  │(Redis) │  │
│  └────────┘  └──────┘  └────────┘  │
└─────────────────────────────────────┘
```

## Scalability Considerations

### Horizontal Scaling
- Multiple agent instances
- Load balancing across APIs
- Distributed task queue

### Vertical Scaling
- Increase memory allocation
- Optimize database queries
- Cache frequently accessed data

### Performance Optimization
- Query optimization
- Memory management
- Caching strategies

## Security Architecture

```
┌────────────────────────────────────┐
│   Permission System                │
│  - Centralized control             │
│  - Audit logging                   │
│  - Policy enforcement              │
└────────────────────────────────────┘
   │
   ▼
┌────────────────────────────────────┐
│   Component Security               │
│  - Input validation                │
│  - Error handling                  │
│  - Exception management            │
└────────────────────────────────────┘
   │
   ▼
┌────────────────────────────────────┐
│   Storage Security                 │
│  - Encryption at rest              │
│  - Secure credentials              │
│  - Audit trails                    │
└────────────────────────────────────┘
```

## Future Enhancements

### Planned Features
1. Multi-user support with authentication
2. Distributed agent architecture
3. Advanced NLP with transformers
4. Reinforcement learning capabilities
5. Real-time collaboration
6. Cloud integration
7. Advanced visualization
8. Web-based UI

### Scalability Plans
1. Microservices architecture
2. Message queuing (RabbitMQ, Kafka)
3. Distributed memory (Redis, Memcached)
4. Multi-tenant support
5. Advanced monitoring and observability

---

REX Architecture v1.0 - Production-Ready AI System
