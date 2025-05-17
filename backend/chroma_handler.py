import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings(persist_directory=".chromadb"))
try:
    collection = client.get_collection(name="chat-memory")
except Exception:
    collection = client.create_collection(name="chat-memory")

def save_to_memory(user_msg, bot_msg):
    collection.add(documents=[user_msg + " " + bot_msg], ids=[str(len(collection.get()["ids"]))])

def get_context(query):
    results = collection.query(query_texts=[query], n_results=3)
    return " ".join(results["documents"][0]) if results["documents"] else ""
