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

## 🛠️ Installation & Getting Started

### Prerequisites

Ensure you have the following installed on your system:
- **Node.js** (v18 or higher) for the frontend dashboard.
- **Python** (v3.10 or higher) for the AI kernel and backend.
- **Git**

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/omni-x.git
cd omni-x
```

### 2. Environment Configuration

Create a `.env` file to store your protected variables. If a `.env.example` is provided, you can copy it:

```bash
cp .env.example .env
```
Ensure you add a valid `GEMINI_API_KEY` (or the respective provider key you plan to use) in the `.env` file to power the foundation models.

### 3. Backend Setup (Kernel OS)

The core OS architecture runs on Python. To initialize the FastAPI backend:

```bash
# Navigate to the backend directory (if separated)
cd omnimesh-x

# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install the dependencies
make install
# Alternatively, you can use: pip install -e .

# Boot the OS backend server
make run
# Alternatively, you can run the raw script: ./scripts/launch_api.sh
```
*The backend API will start on `http://localhost:8000` (or the designated port).*

### 4. Frontend Setup (React Dashboard)

Open a **new terminal tab/window**, keep the backend running, and initialize the frontend dashboard UI from the project root:

```bash
# Install Node dependencies
npm install

# Launch the Vite development server
npm run dev
```

### 5. Usage

1. **Access the Interface:** Open your browser and navigate to the local Frontend URL (typically `http://localhost:3000` or `http://localhost:5173`).
2. **Review Metrics:** Check the **System Pulse** and telemetry states to ensure the Node-to-Backend connection is fully active.
3. **Execute:** The dashboard connects to the background Python API (FastAPI) which acts as the core operating system layer. You can monitor reasoning loops, execution paths, and memory retrieval directly via the UI or by interacting with the backend REST endpoints.

---
*Built openly as a true OS framework. No proprietary boundaries.*
