import requests

OLLAMA_API = "http://localhost:11434/api/generate"  #local

def summarize_memo(memo: str) -> str:
    payload = {
        "model": "gpt-oss:20b-cloud",
        "prompt": f"Tóm tắt nội dung cuộc họp sau:\n\n{memo}\n\nTóm tắt:",
        "stream": False
    }
    resp = requests.post(OLLAMA_API, json=payload)
    return resp.json().get("response", "")

def answer_question(question: str, context: str) -> str:
    payload = {
        "model": "gpt-oss:20b-cloud",
        "prompt": f"Dựa trên nội dung sau:\n{context}\n\nCâu hỏi: {question}\n\nTrả lời:",
        "stream": False
    }
    resp = requests.post(OLLAMA_API, json=payload)
    return resp.json().get("response", "")
