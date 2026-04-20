import os

struct = [
    "omnimesh-x/docs/architecture",
    "omnimesh-x/docs/safety",
    "omnimesh-x/docs/runbooks",
    "omnimesh-x/configs/global",
    "omnimesh-x/data",
    "omnimesh-x/tokenizer",
    "omnimesh-x/apps/operator_console",
    "omnimesh-x/infra",
    "omnimesh-x/scripts",
    "omnimesh-x/checkpoints",
    "omnimesh-x/experiments",
    "omnimesh-x/tests/unit",
    "omnimesh-x/src/omnimesh_x/foundation",
    "omnimesh-x/src/omnimesh_x/multimodal",
    "omnimesh-x/src/omnimesh_x/reasoning",
    "omnimesh-x/src/omnimesh_x/memory",
    "omnimesh-x/src/omnimesh_x/agents",
    "omnimesh-x/src/omnimesh_x/tools",
    "omnimesh-x/src/omnimesh_x/safety",
    "omnimesh-x/src/omnimesh_x/alignment",
    "omnimesh-x/src/omnimesh_x/routing",
    "omnimesh-x/src/omnimesh_x/providers",
    "omnimesh-x/src/omnimesh_x/inference",
    "omnimesh-x/src/omnimesh_x/training",
    "omnimesh-x/src/omnimesh_x/evals",
    "omnimesh-x/src/omnimesh_x/observability",
    "omnimesh-x/src/omnimesh_x/governance",
    "omnimesh-x/src/omnimesh_x/deployment",
    "omnimesh-x/src/omnimesh_x/schemas",
    "omnimesh-x/src/omnimesh_x/services",
    "omnimesh-x/src/omnimesh_x/utils",
]

for d in struct:
    os.makedirs(d, exist_ok=True)

files = {
    "omnimesh-x/pyproject.toml": """[project]
name = "omnimesh-x"
version = "0.1.0"
description = "OmniMesh X - Multimodal Agentic AI OS"
authors = [{name = "OmniMesh Team"}]
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "fastapi>=0.100",
    "uvicorn>=0.23",
    "pydantic>=2.4",
    "pydantic-settings>=2.0",
    "structlog>=23.1",
]
""",
    "omnimesh-x/README.md": """# OmniMesh X
A multimodal, agentic AI operating system that can reason, plan, retrieve memory, use tools, coordinate specialist agents, route across model providers, enforce safety policies, and operate under full observability.
""",
    "omnimesh-x/src/omnimesh_x/__init__.py": "__version__ = '0.1.0'",
    "omnimesh-x/src/omnimesh_x/settings.py": """from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    environment: str = "local"
    log_level: str = "INFO"
    default_provider: str = "mock"

    class Config:
        env_file = ".env"

settings = Settings()
""",
    "omnimesh-x/src/omnimesh_x/schemas/__init__.py": "",
    "omnimesh-x/src/omnimesh_x/schemas/api.py": """from pydantic import BaseModel
from typing import Optional, Dict, Any

class TaskRequest(BaseModel):
    prompt: str
    task_type: Optional[str] = "general"
    use_tools: bool = False
    context: Optional[str] = None

class TaskResponse(BaseModel):
    content: str
    provider_used: str
    trace_id: str
    metadata: Dict[str, Any] = {}
""",
    "omnimesh-x/src/omnimesh_x/providers/__init__.py": "",
    "omnimesh-x/src/omnimesh_x/providers/base.py": """from abc import ABC, abstractmethod
from ..schemas.api import TaskRequest, TaskResponse

class BaseProvider(ABC):
    provider_name: str

    @abstractmethod
    async def generate(self, request: TaskRequest) -> TaskResponse:
        pass

    @abstractmethod
    async def healthcheck(self) -> bool:
        pass
""",
    "omnimesh-x/src/omnimesh_x/providers/mock_adapter.py": """import uuid
from .base import BaseProvider
from ..schemas.api import TaskRequest, TaskResponse

class MockProvider(BaseProvider):
    provider_name = "mock"

    async def generate(self, request: TaskRequest) -> TaskResponse:
        return TaskResponse(
            content=f"[Mock Response] Trace executing... Simulated logic for: '{request.prompt[:50]}'",
            provider_used=self.provider_name,
            trace_id=str(uuid.uuid4()),
            metadata={"status": "success", "latency_ms": 15}
        )

    async def healthcheck(self) -> bool:
        return True
""",
    "omnimesh-x/src/omnimesh_x/routing/__init__.py": "",
    "omnimesh-x/src/omnimesh_x/routing/router.py": """from ..schemas.api import TaskRequest, TaskResponse
from ..providers.mock_adapter import MockProvider

class Router:
    def __init__(self):
        # In later phases, this acts as an intelligence exchange
        self.providers = {
            "mock": MockProvider()
        }

    async def route_and_execute(self, request: TaskRequest) -> TaskResponse:
        # Phase 1: Basic static routing. Later involves heuristic matching.
        provider = self.providers.get("mock")
        if not provider:
            raise ValueError("No eligible provider available.")
            
        return await provider.generate(request)
""",
    "omnimesh-x/src/omnimesh_x/deployment/__init__.py": "",
    "omnimesh-x/src/omnimesh_x/deployment/api_server.py": """from fastapi import FastAPI
from ..schemas.api import TaskRequest, TaskResponse
from ..routing.router import Router

app = FastAPI(title="OmniMesh X Core", version="0.1.0")
router = Router()

@app.post("/v1/generate", response_model=TaskResponse)
async def generate(request: TaskRequest):
    # Phase 1 Flow: Receive -> Route -> Execute -> Return
    response = await router.route_and_execute(request)
    return response

@app.get("/health")
async def health():
    return {"status": "ok", "system": "OmniMesh X"}
""",
    "omnimesh-x/Makefile": """dev:
	cd src && uvicorn omnimesh_x.deployment.api_server:app --reload --port 8000
test:
	pytest tests/
""",
    "omnimesh-x/scripts/launch_api.sh": """#!/bin/bash
cd src && uvicorn omnimesh_x.deployment.api_server:app --reload --port 8000
"""
}

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

os.chmod("omnimesh-x/scripts/launch_api.sh", 0o755)
print("OmniMesh X Level 1 successfully constructed.")
