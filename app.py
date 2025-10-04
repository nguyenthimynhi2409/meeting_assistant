from fastapi import FastAPI, Body
from pydantic import BaseModel
import uuid

from services.ollama_client import summarize_memo, answer_question
from services.chroma_client import save_meeting, search_context, list_meetings

app = FastAPI()

class MemoRequest(BaseModel):
    memo: str

class QuestionRequest(BaseModel):
    question: str

@app.post("/upload_memo")
def upload_memo(req: MemoRequest):
    meeting_id = str(uuid.uuid4())
    summary = summarize_memo(req.memo)
    save_meeting(meeting_id, req.memo, summary)
    return {"meeting_id": meeting_id, "summary": summary}

@app.post("/ask_question")
def ask_question(req: QuestionRequest):
    docs, metas = search_context(req.question)
    context = "\n".join(docs + [m.get("summary", "") for m in metas])
    answer = answer_question(req.question, context)
    return {"answer": answer, "context_used": context}

@app.get("/meetings")
def get_meetings():
    data = list_meetings()
    meetings = []
    for doc, meta, id_ in zip(data["documents"], data["metadatas"], data["ids"]):
        meetings.append({
            "id": id_,
            "summary": meta.get("summary", ""),
            "memo": doc
        })
    return {"meetings": meetings}
