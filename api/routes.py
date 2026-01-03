from fastapi import APIRouter
from pydantic import BaseModel
from core.embedding import EmbeddingService
from storage.base import DocumentStore
from core.retriever import Retriever
from core.answer import AnswerGeneration
from graph.workflow import build_workflow
from core.app_state import AppState

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

class DocumentRequest(BaseModel):
    text: str


def register_routes(router: APIRouter, store: DocumentStore, embedding: EmbeddingService,  retriever: Retriever, answer: AnswerGeneration, app_state: AppState) -> None:

    workflow = build_workflow(retriever, answer) 

    @router.post("/ask")
    def ask(req: QuestionRequest):
        result = workflow.invoke({
            "question" : req.question
        })
        return {"question" : req.question, "context" : result['context'], "answer" : result['answer']}

    @router.post("/add")
    def add(req: DocumentRequest):
        vector = embedding.embed(req.text)
        doc_id = hash(req.text)
        store.add(doc_id, req.text, vector)
        return {"status": "added", "doc_id": doc_id}
    
    @router.get("/status")
    def status():
        return {
            "storage": "qdrant" if app_state.is_using_qdrant() else "in_memory",
            "documents_count": app_state.documents_count(),
            "service": "ready"
        }