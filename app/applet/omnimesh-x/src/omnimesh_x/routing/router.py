from ..schemas.api import TaskRequest, TaskResponse
from ..providers.mock_adapter import MockProvider

class Router:
    def __init__(self):
        # In advanced phases (Level 3), this acts as a dynamic intelligence framework
        self.providers = {
            "mock": MockProvider()
        }

    async def route_and_execute(self, request: TaskRequest) -> TaskResponse:
        # Phase 1 Basic Routing Logic
        provider = self.providers.get("mock")
        if not provider:
            raise ValueError("No eligible provider available.")
            
        return await provider.generate(request)
