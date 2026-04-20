from abc import ABC, abstractmethod
from ..schemas.api import TaskRequest, TaskResponse

class BaseProvider(ABC):
    provider_name: str

    @abstractmethod
    async def generate(self, request: TaskRequest) -> TaskResponse:
        pass

    @abstractmethod
    async def healthcheck(self) -> bool:
        pass
