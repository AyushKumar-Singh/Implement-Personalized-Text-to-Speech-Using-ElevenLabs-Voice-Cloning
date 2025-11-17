# 🎙️ Personalized Text-to-Speech System (ElevenLabs Voice Cloning)  
**AI Voice Cloning • Natural Speech Synthesis • Multi-Mode TTS Engine**

This project implements a **personalized text-to-speech (TTS)** system using the **ElevenLabs Voice Cloning API**.  
It allows users to generate **natural-sounding speech** in a cloned voice with configurable parameters, batch conversions, and real-time audio playback.

Designed as a modular, production-ready Python project with clean architecture, error handling, environment isolation, and extendable components.

---

## 🚀 Key Features

### 🔊 **Voice Cloning & Speech Generation**
- Uses ElevenLabs advanced voice cloning API  
- Produces highly natural and expressive TTS output  
- Generates speech in real-time or via file output  

### 🛠️ **Multiple Operation Modes**
- **Quick TTS** → Convert a single text input  
- **Batch Conversion** → Convert multiple lines/files at once  
- **Voice Quality Testing** → Try multiple parameter profiles (stability, similarity, style)

### 🎧 **Audio Playback**
- Uses pygame for instant playback  
- Supports file playback and byte-stream playback  

### ⚙️ **Configurable Voice Parameters**
- Stability (0–1)  
- Similarity Boost (0–1)  
- Style (0–1)  
- Speaker Boost (On/Off)  

### 🧩 **Modular Architecture**
- Clean separation of config, engine, audio manager, and main interface  
- Easy to extend with new TTS providers or UI systems  

---

## 📂 Project Structure

```
Personalized-TTS-System/
├── main.py              # Interactive console interface
├── tts_engine.py        # ElevenLabs TTS integration & streaming
├── audio_manager.py     # Audio playback handler (pygame)
├── config.py            # Environment variables, paths, voice settings
├── requirements.txt     # Dependencies
├── .env                 # API keys & voice ID (ignored by Git)
└── audio_outputs/       # Generated speech files
```

---

## 🔐 Environment Setup

Create a `.env` file in the project root:

```env
ELEVENLABS_API_KEY=your_api_key_here
DEFAULT_VOICE_ID=your_voice_id_here
```

⚠️ **Never commit `.env` to Git.**  
Your `.gitignore` already protects sensitive files.

---

## 📦 Installation

```bash
# Clone repo
git clone <your-repo-url>
cd Personalized-TTS-System

# Create virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Launch the interactive console:

```bash
python main.py
```

You will be presented with three options:

### 1️⃣ **Quick TTS Mode**  
Enter any text → system generates and plays it instantly.

### 2️⃣ **Batch Mode**  
Provide a file or multiple text lines → system processes them sequentially.

### 3️⃣ **Voice Quality Tester**  
Test multiple parameter combinations to fine-tune voice output.

---

## 🧠 Voice Parameter Tuning

The system supports high-flexibility adjustments:

| Parameter          | Range     | Description                                      |
|-------------------|-----------|--------------------------------------------------|
| Stability         | 0.0–1.0   | Controls consistency & smoothness               |
| Similarity Boost  | 0.0–1.0   | Enhances similarity to original cloned voice     |
| Style             | 0.0–1.0   | Controls expressiveness                          |
| Speaker Boost     | On/Off    | Enhances clarity & projection                   |

Configure defaults in **config.py** or override interactively.

---

## 🧰 Technologies Used

- **Python 3.8+**
- **ElevenLabs API**
- **pygame** – audio playback
- **pydub** – audio processing
- **python-dotenv** – env variable management
- **rich** – modern console UI
- **requests** – API client

---

## 🧪 Logging & Error Handling
- Detailed logs stored in `/logs` (if enabled)
- Graceful fallback if API fails or rate limits occur
- Clear terminal feedback powered by **rich**

---

## 🌍 Example Usage

### Quick TTS:
```bash
"Hello Ayush, your personalized voice system is active."
```

### Batch Mode:
```
Enter the path of a text file:
sentences.txt
```

### Parameter Test Mode:
- Try low stability  
- Try high similarity  
- Compare output differences  

---

## 📚 Useful Resources

- ElevenLabs API Docs → https://api.elevenlabs.io/docs  
- pygame Documentation → https://www.pygame.org/docs/  
- pydub Documentation → https://pydub.com/  
- rich Library → https://rich.readthedocs.io/  

---

## 💡 Author  
**Ayush Kumar Singh**  
AI / Automation Engineer • Cloud AI • LangChain • AutoGen • Full-Stack Intelligent Systems

---

## 📝 License  
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## ⚠️ Notes  
- Ensure sufficient ElevenLabs credits  
- Save API keys only in `.env`  
- Check write permissions for `audio_outputs`  
- Large texts may take longer to process  

---

