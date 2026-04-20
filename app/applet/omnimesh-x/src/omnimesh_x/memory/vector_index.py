from abc import ABC, abstractmethod
from typing import List, Dict, Any

class VectorIndex(ABC):
    @abstractmethod
    async def insert(self, text: str, metadata: dict) -> str:
        pass

    @abstractmethod
    async def search(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        pass

class LocalMockIndex(VectorIndex):
    def __init__(self):
        self.store = []

    async def insert(self, text: str, metadata: dict) -> str:
        self.store.append({"text": text, "metadata": metadata})
        return f"doc_{len(self.store)}"

    async def search(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        return self.store[:top_k]
