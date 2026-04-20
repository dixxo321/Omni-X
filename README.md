# OmniMesh X

OmniMesh X is a multimodal, agentic AI operating system that can reason, plan, retrieve memory, use tools, coordinate specialist agents, route across model providers, enforce safety policies, and operate under full observability. The architecture is engineered to run seamlessly via secure Action-Gated execution while providing robust ecosystem-level intelligence.

## 🚀 Architecture Highlights

### Level 1: Foundation & Base Abstractions
* **API Server:** High-performance REST architecture built with FastAPI.
* **Provider Routing:** Dynamic execution routing between foundation models (`MockAdapter`, `Gemini`, `vLLM`).
* **Settings Management:** Strictly typed Pydantic configuration and schema enforcement.

### Level 2: Cognition, Memory & Safety
* **Reasoning:** Task planner and verifier capable of breaking complex objectives into structured node graphs.
* **Safety Governors (`ActionGate`):** Enforces rigorous privilege controls, stopping unverified or dangerous payloads dynamically.
* **Vector Memory (`LocalMockIndex`):** Built-in abstract interfaces and mocked indices for semantic vector search.
* **Observability:** Granular execution tracing mapping system latency, token consumption, and action flow.
* **Classifiers:** `CyberMisuseClassifier` identifies hostile prompt injection before touching inference pipelines.

### Level 3: Advanced Intelligence & Ecosystem
* **Agents:** Specialist `CodeAgent` running AST sand-boxing and progressive repair loops, managed by an orchestral `ExecutiveAgent`.
* **Tools (`PythonTool`, `BashTool`):** Hyper-restricted sandbox containers preventing system imports and destructive binaries natively at execution.
* **Alignment:** Embedded Reward Mode mechanisms bridging RLHF/DPO logic to shape continuous model safety vs. helpfulness dynamics.
* **Inference Pipeline:** Foundational multi-layer transformer blueprints supporting KV-caching logic structure.
* **Release Matrices:** Automated evaluation harness driving gate-release telemetry.

## 🔥 Dashboard Integration
The system integrates an adaptive **Sophisticated Dark** React dashboard mapping actual pulse telemetry, tracing output states, and global node saturation directly to the kernel layer.

## ⚙️ Initializing the System

1. Install backend requirements via `make install`.
2. Initialize the background API: `make run` or `.scripts/launch_api.sh`
3. Launch the web UI via `npm run dev`.

---
*Built openly as a true OS framework. No proprietary boundaries.*
