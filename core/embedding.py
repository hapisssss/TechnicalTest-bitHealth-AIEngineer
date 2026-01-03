import random
from typing import List


class EmbeddingService:
    
    def embed(self, text: str) -> List[float]:
        random.seed(abs(hash(text)) % 10000)
        return [random.random() for _ in range(128)]