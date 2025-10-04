# 📝 Meeting Assistant (FastAPI + Ollama + ChromaDB)

## 🚀 1. Cài đặt

Cài dependencies:

```bash
pip install -r requirements.txt
```

File `requirements.txt`:

```txt
fastapi
uvicorn
chromadb
requests
pydantic
```

---

## ▶️ 2. Chạy server

```bash
uvicorn app:app --reload
```

Mặc định server sẽ chạy ở **http://127.0.0.1:8000**

Docs API có sẵn tại:
- Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 3. Test API với mock input

### **Cách 1: Swagger UI**
1. Mở [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Dùng thử 3 endpoint:
   - `POST /upload_memo`
   - `POST /ask_question`
   - `GET /meetings`

#### Ví dụ Input (upload memo)
```json
{
  "memo": "Cuộc họp ngày 3/10: Team frontend báo cáo tiến độ migration sang React 18. \\
API backend còn chậm nên bị block một số task. \\
Team QA phát hiện 5 bug liên quan đến form validation. \\
Kế hoạch tuần tới: fix bug và optimize API."
}
```

---

### **Cách 2: Dùng curl**

**Upload memo**
```bash
curl -X POST "http://127.0.0.1:8000/upload_memo" \\
     -H "Content-Type: application/json" \\
     -d '{"memo": "Cuộc họp ngày 3/10: Team frontend báo cáo tiến độ migration sang React 18. API backend còn chậm nên bị block. QA phát hiện 5 bug. Kế hoạch: fix bug và optimize API."}'
```

**Ask question**
```bash
curl -X POST "http://127.0.0.1:8000/ask_question" \\
     -H "Content-Type: application/json" \\
     -d '{"question": "Tuần tới team sẽ làm gì?"}'
```

**List meetings**
```bash
curl "http://127.0.0.1:8000/meetings"
```

---

### **Cách 3: Script test**

Chạy file `test_api.py`:

```bash
python test_api.py
```

📌 Kết quả mock output (ví dụ):

```json
=== Upload Memo ===
{
  "meeting_id": "8c1f18c3-ff4d-4e4d-9cda-7e41d9035c20",
  "summary": "Frontend migration React 18 bị block do API backend. QA tìm thấy 5 bug. Tuần tới sẽ fix bug và tối ưu API."
}

=== Ask Question ===
{
  "answer": "Tuần tới team sẽ fix 5 bug form validation và tối ưu API backend.",
  "context_used": "Frontend migration React 18 ... QA phát hiện 5 bug ... Kế hoạch: fix bug và optimize API."
}

=== Get Meetings ===
{
  "meetings": [
    {
      "id": "8c1f18c3-ff4d-4e4d-9cda-7e41d9035c20",
      "summary": "Frontend migration React 18 bị block do API backend. QA tìm thấy 5 bug. Tuần tới sẽ fix bug và tối ưu API.",
      "memo": "Cuộc họp ngày 3/10: Team frontend báo cáo tiến độ migration sang React 18..."
    }
  ]
}
```