from langgraph.graph import StateGraph, END
from core.retriever import Retriever
from core.answer import AnswerGeneration
from core.embedding import EmbeddingService
from storage.memory_store import InMemoryDocumentStorage


def build_workflow(retriever: Retriever, answer: AnswerGeneration) -> StateGraph:

    def retrieve_node(state: dict):
        state["context"] = retriever.retrieve(state['question'], 2)
        return state

    def answer_node(state: dict):
        state["answer"] = answer.answer(state["context"])
        return state

    graph = StateGraph(dict)
    graph.add_node("retrieve", retrieve_node)
    graph.add_node("answer", answer_node)
    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "answer")
    graph.add_edge("answer", END)

    return graph.compile()









# embbed = EmbeddingService()

# docs = {}
# store = InMemoryDocumentStorage(docs)

# retrieve = Retriever(embbed,store)

# answer = AnswerGeneration()



# chain = build_workflow(retriever=retrieve,answer=answer)

# # add document
# text = "RAG stands for Retrieval Augmented Generation"
# vector = embbed.embed(text)
# store.add(1, text, vector)

# # ask
# result = chain.invoke({
#     "question": "What is RAG?"
# })

# print(result["answer"])






    
    