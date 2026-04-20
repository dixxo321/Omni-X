import uuid
from .base import BaseProvider
from ..schemas.api import TaskRequest, TaskResponse

class MockProvider(BaseProvider):
    provider_name = "mock"

    async def generate(self, request: TaskRequest) -> TaskResponse:
        return TaskResponse(
            content=f"[Mock Mode] Tracked logical reasoning for input: '{request.prompt[:50]}...'",
            provider_used=self.provider_name,
            trace_id=str(uuid.uuid4()),
            metadata={"status": "success", "latency": "30ms"}
        )

    async def healthcheck(self) -> bool:
        return True
