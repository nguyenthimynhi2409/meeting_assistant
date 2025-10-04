import chromadb

chroma_client = chromadb.PersistentClient(path="./db/chroma_store")
collection = chroma_client.get_or_create_collection("meetings")

def save_meeting(meeting_id: str, memo: str, summary: str):
    collection.add(
        documents=[memo],
        metadatas=[{"summary": summary}],
        ids=[meeting_id]
    )

def search_context(question: str, top_k: int = 2):
    results = collection.query(query_texts=[question], n_results=top_k)
    docs = results.get("documents", [[]])[0]
    metas = results.get("metadatas", [[]])[0]
    return docs, metas

def list_meetings():
    results = collection.get()
    return results
