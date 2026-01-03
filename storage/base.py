from abc import ABC
from typing import List

class DocumentStore(ABC):

    @classmethod
    def add(self, doc_id: int, text: str, vector: List[float]) -> None:
        pass

    @classmethod
    def search(self, vector: List[float], limit: int) -> List[str]:
        pass