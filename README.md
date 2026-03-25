# 🧠 Smart Notes AI (Offline)

An AI-powered note-taking system that lets you **store, search, and chat with your notes — completely offline**.

---

## 🚀 Features

* 📝 Add and store notes
* 🔍 Semantic search (not keyword-based)
* 💬 Chat with your notes (AI-powered)
* ⚡ Fast retrieval using FAISS
* 🎨 Clean terminal UI with Rich
* 🔒 Fully offline (no API keys required)

---

## 🧠 How It Works

This project uses a **RAG (Retrieval-Augmented Generation)** pipeline:

1. Notes are converted into embeddings
2. Stored in a FAISS vector database
3. User query is embedded
4. Most relevant notes are retrieved
5. A local LLM generates the final answer

---

## 📁 Project Structure

```
smart_notes_ai/
│
├── main.py
├── embedder.py
├── database.py
├── ai.py
├── notes/
├── index/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/smart-notes-ai.git
cd smart-notes-ai
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## 🤖 Setup Local AI (Ollama)

Install Ollama and run:

```
ollama run llama3
```

This downloads and runs a local language model.

---

## ▶️ Usage

Run the app:

```
python main.py
```

### Menu Options:

* Add Note
* Search Notes
* Chat with Notes
* View Stats

---

## 🧪 Example

**Stored Notes:**

```
Python is used for AI
Newton's laws explain motion
```

**Query:**

```
What explains motion?
```

**Output:**

```
Newton's laws explain motion.
```

---

## 📦 Requirements

```
sentence-transformers
faiss-cpu
rich
numpy
requests
```

---

## 🚀 Future Improvements

* 📂 File ingestion (PDF, TXT, Markdown)
* 🧠 Better ranking (cosine similarity)
* 💬 Streaming responses
* 🖥 GUI version
* 🔗 Chat memory
* ⚡ Local LLM optimization

---

## ⚠️ Notes

* Requires Ollama running locally for chat mode
* Works best with meaningful, full-sentence notes
* Small datasets may give weaker results

---

## 📜 License

MIT License

---

## 💡 Inspiration

Built as a **local alternative to AI note tools**, focused on:

* Privacy
* Speed
* Simplicity

---

## 👨‍💻 Author

Built by a student exploring AI + development 🚀
