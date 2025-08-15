
# Noir — Cross-Platform Voice Assistant

Noir is a Python-based, cross-platform voice assistant that works **online and offline**.  
It integrates cloud AI providers (OpenAI, Perplexity) for rich responses when online,  
and uses local models (Ollama, Vosk, Piper) when offline — so you always get an answer.

---

## ✨ Features
- 🎤 **Speech to Text (STT)**  
  - **Online**: OpenAI Whisper API  
  - **Offline**: Vosk  
- 💬 **Conversational AI**  
  - **Online**: OpenAI, Perplexity  
  - **Offline**: Local LLM via Ollama / llama.cpp  
- 🔊 **Text to Speech (TTS)**  
  - **Online**: Microsoft Edge TTS  
  - **Offline**: Piper  
- 🖥️ **Cross-Platform Clients**  
  - **Desktop**: PySide6 GUI  
  - **Android**: Kivy/KivyMD app  

---

## 📂 Project Structure
---
noir/
├─ server/
│  ├─ __init__.py
│  ├─ main.py               # FastAPI entry point
│  ├─ config.py             # API keys, settings
│  ├─ routes/
│  │   ├─ __init__.py
│  │   ├─ assist.py         # /v1/assist (chat logic)
│  │   ├─ stt.py            # /v1/stt (speech to text)
│  │   ├─ tts.py            # /v1/tts (text to speech)
│  ├─ services/
│  │   ├─ __init__.py
│  │   ├─ openai_api.py     # Calls to OpenAI
│  │   ├─ perplexity_api.py # Calls to Perplexity
│  │   ├─ offline_llm.py    # Local LLM (Ollama, llama.cpp, etc.)
│  │   ├─ vosk_stt.py       # Offline STT
│  │   ├─ whisper_stt.py    # OpenAI Whisper API
│  │   ├─ piper_tts.py      # Offline TTS
│  │   ├─ edge_tts.py       # Cloud TTS fallback
│  └─ utils/
│      ├─ audio.py          # Audio processing helpers
│      ├─ model_selector.py # Picks model based on mode (online/offline)
│
├─ client/
│  ├─ desktop/              # PySide6 GUI app
│  │   ├─ main.py
│  │   ├─ ui_main.py
│  │   ├─ recorder.py
│  │   ├─ player.py
│  │   ├─ api_client.py
│  │
│  ├─ android/              # Kivy/KivyMD mobile app
│  │   ├─ main.py
│  │   ├─ recorder.py
│  │   ├─ player.py
│  │   ├─ api_client.py
│
├─ tests/
│  ├─ test_assist.py
│  ├─ test_stt.py
│  ├─ test_tts.py
│
├─ requirements.txt
├─ README.md
├─ .env.example
└─ run.sh
---
## ⚙️ Requirements

### System Dependencies
- **Python 3.10+**
- `ffmpeg` (audio processing)
- **Offline Models** *(optional for offline mode)*:
  - [Vosk model](https://alphacephei.com/vosk/models)
  - [Piper voice model](https://github.com/rhasspy/piper)
  - [Ollama](https://ollama.ai/) or `llama.cpp`

### Python Dependencies
```bash
pip install -r requirements.txt
````

Example `requirements.txt`:

```
fastapi
uvicorn
requests
pydantic
vosk
pyaudio
PySide6
kivy
kivymd
```

---

## 🚀 Running Noir

### 1️⃣ Backend

```bash
uvicorn server.main:app --reload --port 8000
```

### 2️⃣ Desktop Client

```bash
cd client/desktop
python main.py
```

### 3️⃣ Android Client

```bash
cd client/android
python main.py
# (or build APK with buildozer)
```

---

## 🌐 API Endpoints

| Method | Endpoint     | Description     |
| ------ | ------------ | --------------- |
| POST   | `/v1/stt`    | Speech → Text   |
| POST   | `/v1/assist` | Get AI response |
| POST   | `/v1/tts`    | Text → Speech   |
| GET    | `/`          | Health check    |

---

## 🔐 Configuration

Copy `.env.example` → `.env` and fill in your keys:

```
OPENAI_API_KEY=your_openai_key
PERPLEXITY_API_KEY=your_perplexity_key
OFFLINE_LLM_BASE_URL=http://localhost:11434
OFFLINE_LLM_MODEL=llama2
```

---

## 🛠 Development Notes

* When **offline**, Noir automatically switches to local STT/LLM/TTS.
* Clients and backend communicate over HTTP/WebSocket for real-time interaction.
* Audio formats: `WAV` for STT, `MP3`/`WAV` for TTS.

---

## 📜 License

MIT License — do whatever you want, just keep the credits.

---

## 📌 Roadmap

* [ ] Add hotword detection ("Hey Noir")
* [ ] Add browser extension
* [ ] Add knowledge graph integration
* [ ] Improve multi-turn memory


