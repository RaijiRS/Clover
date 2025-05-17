from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .ollama_handler import generate_response
from .chroma_handler import save_to_memory, get_context
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory store of sessions (you can replace this with a database later)
sessions = {}

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body["message"]
    conversation_id = body.get("conversation_id")

    if not conversation_id or conversation_id not in sessions:
        conversation_id = str(uuid.uuid4())
        sessions[conversation_id] = []

    # Add to session history
    sessions[conversation_id].append({"role": "user", "content": user_input})

    # Create context from memory or session history
    context = get_context(user_input) or "\n".join(
        [msg["content"] for msg in sessions[conversation_id] if msg["role"] == "user"]
    )

    # Get AI response
    response = generate_response(user_input, context)

    # Save response to session
    sessions[conversation_id].append({"role": "assistant", "content": response})

    # Persist if needed
    save_to_memory(user_input, response)

    return {"response": response, "conversation_id": conversation_id}
