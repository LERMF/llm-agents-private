# LLM Agents Private

> **Asymmetric 3-agent swarm operating over a compressed inter-machine dialectic.**

```
               ┌────────────────────────────────────────────────┐
               │                  Orchestrator                  │
               │         (State Coordinator & Synthesizer)      │
               └───────────────▲────────────────▲───────────────┘
                               │                │
            [Compressed Wire]  │                │  [Compressed Wire]
                               ▼                ▼
                     ┌──────────────────┐  ┌──────────────────┐
                     │    Researcher    │  │      Coder       │
                     │  (Ollama Local)  │  │   (Groq Speed)   │
                     └──────────────────┘  └──────────────────┘
                               │
                        [Human Gate] ──► Explicit expansion (`EXPAND:`)
```

When multi-agent architectures scale, chat volume scales quadratically ($O(n^2)$). Standard agent systems force machines to talk to machines in verbose English, consuming context limits on conversational polite filler.

`llm-agents-private` decouples machine-to-machine reasoning from human interface formatting. The 3-agent swarm communicates internally through an ultra-dense compressed wire dialect, only expanding into natural language when an explicit explanation gate is tripped.

---

## ✦ Swarm Roles & Model Assignment

| Agent | Target Model Runtime | Primary Responsibility | Dialectic State |
|---|---|---|---|
| **Researcher** (`researcher.py`) | Ollama (Local) | Document ingestion, vector querying, and background fact retrieval | Strictly Compressed |
| **Coder** (`coder.py`) | Groq (Llama-3-70B Edge) | High-speed AST generation, unit test creation, and diff synthesis | Strictly Compressed |
| **Orchestrator** (`orchestrator.py`) | Multi-Provider Engine | Consensus reconciliation, execution planning, and user interface gate | Dual-Mode Gate |

---

## ✦ Communication Protocol

```python
# agents/researcher.py
from llm_workspace import CompressedLLM

agent = CompressedLLM('ollama')
# Internal cluster transmission remains compressed by default.
# Human output triggers expansion only upon request:
def query_knowledge(topic: str) -> str:
    return agent.call(topic)
```

```python
# agents/orchestrator.py
# Coordinates team via dense token representations.
# Expands output only when user explicitly invokes 'explain' or 'report'.
```

---

## ✦ Architectural Advantages

1. **Context Window Preservation**: Inter-agent exchanges consume $<5\%$ of typical conversational token budgets.
2. **Specialized Inference**: Local models execute low-risk factual extraction; high-speed cloud accelerators generate code.
3. **Audit Readiness**: Full semantic traces remain reconstructible by passing raw wire logs through the decompression gate.

---

## ✦ License
[MIT](LICENSE) © LERMF
