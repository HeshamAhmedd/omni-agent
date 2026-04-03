import chromadb
from sentence_transformers import SentenceTransformer
from datetime import datetime

class BaseMemory:
    def __init__(self, collection_name: str):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.client = chromadb.Client()
        self.collection = self.client.get_or_create_collection(collection_name)

    def _embed(self, text: str) -> list:
        return self.model.encode(text).tolist()

    def search(self, query: str, n: int = 3) -> list:
        results = self.collection.query(
            query_embeddings=[self._embed(query)], n_results=n
        )
        return results["documents"][0]


class SemanticMemory(BaseMemory):
    def __init__(self):
        super().__init__("semantic")

    def remember(self, fact: str, fact_id: str):
        self.collection.upsert(
            ids=[fact_id],
            documents=[fact],
            embeddings=[self._embed(fact)],
        )


class EpisodicMemory(BaseMemory):
    def __init__(self):
        super().__init__("episodic")

    def remember(self, event: str):
        timestamp = datetime.now().isoformat()
        self.collection.add(
            ids=[timestamp],
            documents=[event],
            embeddings=[self._embed(event)],
            metadatas=[{"timestamp": timestamp}],
        )