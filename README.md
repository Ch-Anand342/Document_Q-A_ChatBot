# 📚 Document Q&A Bot using Gemini AI, ChromaDB & Streamlit

An AI-powered Document Question Answering System that allows users to upload documents and ask natural language questions about their content.

The application uses Google's Gemini Embedding Model for semantic search, ChromaDB as a vector database, and Gemini LLM for answer generation.

---

## 🚀 Features

- Upload and process PDF documents
- Automatic document chunking
- Semantic search using vector embeddings
- Retrieval-Augmented Generation (RAG)
- Context-aware question answering
- Fast document retrieval with ChromaDB
- Streamlit-based user interface
- Gemini AI integration
- Multiple document support

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python 3.11

### AI Models
- Gemini 2.5 Flash
- Gemini Embedding 001

### Vector Database
- ChromaDB

### Libraries Used
- Google Generative AI
- PyPDF2
- ChromaDB
- Streamlit
- UUID
- tqdm

## 🔑 Environment Configuration

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Get your Gemini API Key from:

https://aistudio.google.com

---

## 📄 Add Documents

Place all PDF documents inside:

```text
data/
```

Example papers used by me:

```text
data/
├── AI_paper.pdf
├── Research_paper.pdf
└── Urbanization_study.pdf
```

---

## 🧠 Generate Embeddings

Run:

```bash
python src/ingest.py
```

This will:

- Load documents
- Split text into chunks
- Generate embeddings
- Store vectors in ChromaDB

Successful execution:

```text
Saved Successfully
Ingestion Completed
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Application starts at:

```text
http://localhost:8501
```

---

## 🔍 How It Works

### Step 1: Document Loading

PDF documents are extracted and converted into text.

### Step 2: Chunking

Large documents are split into smaller chunks for efficient retrieval.

### Step 3: Embedding Generation

Each chunk is converted into vector embeddings using:

```text
Gemini Embedding 001
```

### Step 4: Vector Storage

Embeddings are stored inside ChromaDB.

### Step 5: User Query

User asks a question.

Example:

```text
What is the main objective of the study?
```

### Step 6: Semantic Search

Relevant chunks are retrieved from ChromaDB.

### Step 7: Answer Generation

Retrieved context is passed to Gemini LLM which generates the final answer.

---

## 📸 Sample Questions

```text
Summarize the document.

What are the key findings?

What methodology was used?

Who are the authors?

What are the future recommendations?

Explain the conclusion.
```

---

## 🎯 Use Cases

- Research Paper Analysis
- Academic Projects
- Knowledge Base Systems
- Internal Company Documentation
- Legal Document Search
- Policy Document Analysis
- Educational Content Assistant

---

## 📈 Future Enhancements

- DOCX Support
- TXT Support
- Multiple File Upload UI
- Chat History
- Source Citations
- Conversation Memory
- FAISS Support
- User Authentication
- Cloud Deployment

---

## 👨‍💻 Author

**Anand Ch**