# 🎙️ Personalized Text-to-Speech System (ElevenLabs Voice Cloning)

This project implements a **Personalized Text-to-Speech (TTS) System** powered by the **ElevenLabs Voice Cloning API**, designed to generate **natural-sounding audio output in a cloned user voice**.
It features an interactive console interface with multiple conversion modes, voice quality testing, and batch processing capabilities.

---

## 🧩 Project Overview

**Goal:**
To develop a system that replicates a user's voice and generates expressive, human-like speech output using ElevenLabs' voice cloning capabilities.

**Core Workflow:**

> Clone voice → Configure API → Convert Text → Generate Speech → Play Output

---

## ⚙️ Project Structure

| File               | Description                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------- |
| `.env`             | Stores environment variables including the ElevenLabs API key and default voice ID.                         |
| `.gitignore`       | Prevents sensitive and unnecessary files (env, cache, audio outputs, logs) from being tracked in Git.       |
| `config.py`        | Manages configuration including API settings, voice parameters, and directory structures.                    |
| `audio_manager.py` | Handles audio playback using pygame, with support for both file and byte-stream inputs.                     |
| `tts_engine.py`    | Core engine interfacing with ElevenLabs API, supporting streaming and voice parameter customization.        |
| `main.py`          | Interactive console application with multiple modes: Quick TTS, Batch Convert, and Voice Quality Testing.    |
| `requirements.txt` | Project dependencies including elevenlabs, pygame, pydub, and other essential packages.                     |

---

## 🚀 Implementation Steps

### 1. Voice Cloning

1. Create an account on [ElevenLabs](https://beta.elevenlabs.io/)
2. Upload voice samples and create your voice clone
3. Get your unique `voice_id` from the platform

### 2. API Setup & Authentication

1. Obtain your **ElevenLabs API key** from the platform
2. Create a `.env` file in the project root:
   ```env
   ELEVENLABS_API_KEY=your_api_key_here
   DEFAULT_VOICE_ID=your_voice_id_here
   ```

### 3. Installation & Setup

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\\Scripts\\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 4. Running the Application

```bash
python main.py
```

The application provides three main features:
1. **Quick TTS**: Convert single text inputs to speech
2. **Batch Convert**: Process multiple text inputs in sequence
3. **Voice Quality Test**: Test different voice settings for optimal output

---

## 🧠 Features & Capabilities

* ✅ Interactive console interface with rich formatting
* ✅ Multiple conversion modes (quick, batch)
* ✅ Voice quality testing with different parameters
* ✅ Configurable voice settings (stability, similarity)
* ✅ Progress tracking and error handling
* ✅ Audio playback controls
* ✅ Logging system for debugging

---

## 🧰 Technologies Used

* **Language:** Python 3.8+
* **API:** ElevenLabs Voice Cloning API
* **Key Libraries:**
  * `elevenlabs` - API integration
  * `pygame` - Audio playback
  * `pydub` - Audio processing
  * `python-dotenv` - Environment management
  * `rich` - Console interface
  * `requests` - HTTP client

---

## 🎯 Voice Settings

The system supports customizable voice parameters:
* **Stability (0.0-1.0)**: Controls output consistency
* **Similarity Boost (0.0-1.0)**: Adjusts similarity to original voice
* **Style (0.0-1.0)**: Controls expressiveness
* **Speaker Boost**: Enhances voice clarity

---

## 📚 Resources

* [ElevenLabs API Documentation](https://api.elevenlabs.io/docs)
* [Python dotenv Documentation](https://pypi.org/project/python-dotenv/)
* [pygame Documentation](https://www.pygame.org/docs/)
* [Rich Documentation](https://rich.readthedocs.io/)

---

## 💡 Author

**Ayush Kumar Singh**
AI/ML + Automation Engineer | LangChain • AutoGen • Cloud AI • Full-Stack Intelligent Systems

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Important Notes

* Ensure you have sufficient API credits on your ElevenLabs account
* Store sensitive information (API keys) in `.env` file
* Check output directory permissions before running
* Audio files are saved in the `audio_outputs` directory