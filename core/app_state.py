class AppState:
    
    def __init__(self, using_qdrant: bool, docs_memory: dict | None):
        self.__using_qdrant = using_qdrant
        self.__docs_memory = docs_memory
    
    def is_using_qdrant(self) -> bool:
        return self.__using_qdrant

    def documents_count(self) -> int | None:
        if self.__docs_memory is None:
            return None
        return len(self.__docs_memory)