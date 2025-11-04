# 🗓️ Meeting Notes & Action Items Extractor

Automatically transform your **meeting audio recordings** into structured outputs:  
✅ **Transcript**  
✅ **Concise Summary**  
✅ **Clear Action Items**  

Built with **open-source, offline-capable models**, this Streamlit app ensures your data stays private—no cloud APIs required (unless you choose to use them). Perfect for teams, freelancers, or students who want to streamline post-meeting workflows.

---

## 🔑 Key Features

- **Audio Upload**: Supports `.mp3`, `.wav`, `.m4a`, and other common formats.
- **Offline Transcription**: Uses **OpenAI Whisper** (CPU-friendly, runs locally).
- **Smart Summarization**: Leverages **Hugging Face Transformers** (e.g., BART) for digestible summaries.
- **Action Item Extraction**:
  - 🔹 **Rule-based**: Keyword-driven identification (e.g., "assign", "due", "need to").
  - 🔹 **LLM-powered (optional)**: Uses **LangChain + Ollama** with local models like `llama2` or `mistral` for deeper semantic understanding.
- **100% Offline Mode**: No internet or API keys needed if using local models only.
- **Clean UI**: Streamlit-powered interface for seamless upload and results viewing.

---

## 🛠️ Tech Stack

| Component             | Technology                         |
|-----------------------|------------------------------------|
| **Frontend**          | Streamlit                          |
| **Transcription**     | OpenAI Whisper (local)             |
| **Summarization**     | Hugging Face `transformers`        |
| **Action Extraction** | Custom logic **or** LangChain + Ollama |
| **LLM Backend**       | Ollama (`llama2`, `mistral`, etc.) |
| **Environment**       | Python 3.10+, `.env` support       |

---

## 📂 Project Structure

```
meeting-notes-extractor/
├── frontend/
│   └── notes.py                # Streamlit UI
├── backend/
│   ├── transcription.py        # Whisper audio → text
│   ├── summarizer.py           # Text → summary
│   └── action_extractor.py     # Summary → action items
├── app.py                      # (Optional main entry)
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (optional)
└── .gitignore
```

---

## ⚙️ Prerequisites

- **Python 3.10+**
- **FFmpeg** (required by Whisper for audio processing)
- **Ollama** (optional, only if using LLM for action items):  
  ```bash
  ollama pull llama2  # or mistral, etc.
  ```

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/lekshmi-c/MeetingNoteExtractor.git
cd meeting-notes-extractor

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
# or
.venv\Scripts\activate           # Windows

# Install core dependencies
pip install -r requirements.txt

# (Optional) Install LangChain + Ollama support
pip install langchain-community langchain-ollama

# Install Whisper (already in requirements.txt, but ensure it's CPU-compatible)
pip install openai-whisper
```

> 💡 **Note**: Whisper runs on CPU by default—no GPU required.

---

## ▶️ Running the App

```bash
streamlit run frontend/notes.py
```

Open your browser to:  
👉 **http://localhost:8501**

---

## 🧪 How to Use

1. **Upload** a meeting audio file (e.g., `team_sync.wav`).
2. The app will:
   - **Transcribe** the audio using Whisper,
   - **Summarize** the full transcript,
   - **Extract action items** using either:
     - Built-in keyword logic, **or**
     - A local LLM (if Ollama is configured).
3. View all three sections clearly in the UI.

---

## ⚙️ Configuration

### Optional: Enable Local LLM for Action Items

1. In `backend/action_extractor.py`, uncomment and configure:
   ```python
   from langchain_ollama import OllamaLLM
   llm = OllamaLLM(model="llama2")
   ```
2. Ensure Ollama is running:
   ```bash
   ollama run llama2
   ```

### Optional: Use OpenAI (Not Recommended for Privacy)

Create a `.env` file:
```env
OPENAI_API_KEY=sk-...
```
> Only needed if you replace local models with OpenAI services (not default).

---

## 📝 Example Output

| Section        | Example |
|----------------|--------|
| **Transcript** | *"We need to finalize the Q3 roadmap by Friday. John will handle the client demo."* |
| **Summary**    | *The team discussed Q3 deliverables and assigned the client demo to John.* |
| **Action Items** | `- Finalize Q3 roadmap by Friday<br>- John: Prepare client demo` |

---

## 🐞 Known Notes

- **First run may be slow**: Models are downloaded and cached on initial use.
- **Large audio files**: Processing time scales with duration (Whisper is CPU-bound).
- **Action item quality**: LLM-based extraction yields richer results than keyword matching.

---

## 🚀 Future Enhancements

- 🎧 **Speaker diarization** (who said what)
- 💾 **Export to Markdown, PDF, or task managers** (e.g., Todoist, Notion)
- 📅 **Auto-schedule reminders** from action items
- 🐳 **Docker support** for one-click deployment

---

## 📄 License

This project is free to use, modify, and distribute. See the repository for full license details.

---

> 💡 **Tip**: Great for stand-ups, client calls, lectures, or interviews—turn hours of audio into actionable insights in minutes, all without leaving your machine!
