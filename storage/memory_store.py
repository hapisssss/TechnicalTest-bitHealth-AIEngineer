from typing import List
from storage.base import DocumentStore

class InMemoryDocumentStorage(DocumentStore):

    def __init__(self, docs: dict):
        self.__docs = docs

    def add(self, doc_id: int, text: str, vector: List[float]) -> None:
        self.__docs[doc_id] = text
    
    def search(self, vector: List[float], limit: int) -> List[str]:
        return  list(self.__docs.values())[:limit]
    

