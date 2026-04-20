from .vector_index import VectorIndex, LocalMockIndex

class RetrievalRouter:
    def __init__(self):
        self.index: VectorIndex = LocalMockIndex()

    async def route_and_retrieve(self, query: str) -> list:
        # Mock conversion of query to an embedding vector
        mock_embedding = [0.05, 0.12, -0.04, 0.99]
        results = await self.index.search(mock_embedding, top_k=3)
        return results
