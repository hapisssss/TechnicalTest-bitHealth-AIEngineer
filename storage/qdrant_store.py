from typing import List
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from storage.base import DocumentStore

class QdrantDocumentStore(DocumentStore):

    def __init__(self, client: QdrantClient, collection: str):
        self.__client = client
        self.__collection = collection
    
    def add(self, doc_id: int, text: str, vector: List[float]) -> None:
        self.__client.upsert(
            collection_name=self.__collection,
            points=[PointStruct(id=doc_id, vector=vector, payload={"text": text})]
        )
    
    def search(self, vector: List[float], limit: int) -> List[str]:
        hits = self.__client.search(
            collection_name=self.__collection,
            query_vector=vector,
            limit=limit
        )
        return [hit.payload["text"] for hit in hits]
    
    
