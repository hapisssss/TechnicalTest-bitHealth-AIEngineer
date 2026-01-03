from typing import List
from core.embedding import EmbeddingService
from storage.base import DocumentStore


class Retriever:
    
    def __init__(self, embedding: EmbeddingService, store: DocumentStore):
        self.__embedding =  embedding
        self.__store = store

    
    def retrieve(self, question: str, limit: int = 2 ) -> List[str]:
        vector = self.__embedding.embed(question)
        return self.__store.search(vector, limit)




