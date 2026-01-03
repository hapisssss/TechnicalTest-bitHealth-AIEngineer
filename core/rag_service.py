from core.answer import AnswerGeneration
from core.retriever import Retriever

class RagService:

    def __init__(self, retriever: Retriever, answer_generator: AnswerGeneration):
        self.__retriever = retriever
        self.__answer_generator = answer_generator

    def ask(self, question: str) -> dict:
        context = self.__retriever.retrieve(question)
        answer = self.__answer_generator.generate(context)

        return {
            "question": question,
            "answer": answer,
            "context_used": context
        }
