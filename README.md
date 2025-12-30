# 🌱 Clover 🍀 — AI Assistant with Memory

**Clover** is a lightweight AI chatbot assistant powered by **FastAPI**, **React**, and **ChromaDB**. It supports file upload, webpage ingestion, contextual chat with memory, and live knowledge injection.

---

## 📦 Features

- 💬 **Stateful AI Chat** - Conversation history with session management
- 📚 **Dynamic Knowledge Base** - Add raw text with source attribution
- 🌐 **Web Page Ingestion** - Load and index web pages automatically
- 📁 **File Upload** - Upload and index `.txt` files
- 🧠 **Vector Search** - Semantic search using ChromaDB
- 🤖 **Local LLM Support** - Powered by Ollama (Mistral or similar models)
- 🔄 **Context-Aware Responses** - Uses vector search to provide relevant context

---

## 🧰 Tech Stack

- **Frontend:** React + Fetch API
- **Backend:** FastAPI (Python)
- **Vector DB:** ChromaDB (with persistence)
- **LLM Inference:** Ollama (Mistral or similar)
- **Embeddings:** Sentence Transformers (via ChromaDB)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+ 
- Node.js and npm
- Ollama installed and running ([Download Ollama](https://ollama.ai))

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/clover.git
cd clover
```

### 2. Backend Setup

#### Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

#### Install Dependencies

```bash
pip install -r requirements.txt
```

#### Start Backend API

```bash
uvicorn backend.main:app --reload
```

The API will be available at `http://localhost:8000`

#### Start Ollama LLM

In a **new terminal** (keep the backend running), activate the virtual environment and run:

```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Run Ollama with Mistral (or your preferred model)
ollama run mistral
```

> **Note:** The code is optimized for Mistral, but you can use other Ollama models. Make sure the model is pulled first: `ollama pull mistral`

### 3. Frontend Setup

In a **new terminal**:

```bash
cd frontend
npm install
npm start
```

The frontend will be available at `http://localhost:3000` (or the port specified by React)

---

## 📡 API Endpoints

### `POST /chat`
Send a message to the AI assistant.

**Request Body:**
```json
{
  "message": "Your question here",
  "conversation_id": "optional-uuid"
}
```

**Response:**
```json
{
  "response": "AI response text",
  "conversation_id": "uuid-string"
}
```

### `POST /add_knowledge`
Add raw text knowledge to the vector database.

**Request Body:**
```json
{
  "text": "Knowledge content here",
  "source": "Source name or URL"
}
```

### `POST /load_webpage`
Load and index a web page.

**Request Body:**
```json
{
  "url": "https://example.com"
}
```

### `POST /get_context`
Retrieve relevant context for a query.

**Request Body:**
```json
{
  "query": "Search query"
}
```

**Response:**
```json
{
  "context": "Retrieved context text"
}
```

### `POST /upload_text_file`
Upload a `.txt` file to be indexed.

**Request:** Multipart form data with `file` field

---

## 📁 Project Structure

```
clover/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── ollama_handler.py    # Ollama integration
│   ├── chroma_handler.py    # ChromaDB operations
│   └── __init__.py
├── frontend/                # React frontend
├── chroma_storage/          # ChromaDB persistent storage
├── venv/                    # Python virtual environment
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🔧 Configuration

### Changing the LLM Model

Edit `backend/ollama_handler.py` to change the model name from `mistral` to your preferred Ollama model.

### ChromaDB Storage

The vector database is persisted in the `chroma_storage/` directory. To reset the knowledge base, delete this directory.

---

## 🐛 Troubleshooting

### Backend won't start
- Ensure the virtual environment is activated
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version: `python --version` (should be 3.8+)

### Ollama connection issues
- Ensure Ollama is running: `ollama list`
- Verify the model is pulled: `ollama pull mistral`
- Check that Ollama is accessible at `http://localhost:11434`

### Frontend connection errors
- Ensure the backend is running on port 8000
- Check CORS settings in `backend/main.py`
- Verify the API URL in frontend configuration

---

## 📝 License

[Add your license here]

---

## 🤝 Contributing

[Add contribution guidelines here]

---

## 📧 Contact

[Add contact information here]
