import os
from pathlib import Path
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional

load_dotenv()

@dataclass
class Config:
    """Application configuration"""
    API_KEY: str
    DEFAULT_VOICE_ID: str
    OUTPUT_DIR: Path
    VOICE_SAMPLES_DIR: Path
    
    # TTS Settings
    DEFAULT_MODEL: str = "eleven_multilingual_v2"
    OUTPUT_FORMAT: str = "mp3_44100_128"
    DEFAULT_STABILITY: float = 0.5
    DEFAULT_SIMILARITY: float = 0.8
    DEFAULT_STYLE: float = 0.0
    USE_SPEAKER_BOOST: bool = True
    
    # API Settings
    API_BASE_URL: str = "https://api.elevenlabs.io/v1"
    REQUEST_TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    
    @classmethod
    def load(cls) -> 'Config':
        """Load configuration from environment"""
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if not api_key:
            raise ValueError("ELEVENLABS_API_KEY not found in environment variables")
        
        return cls(
            API_KEY=api_key,
            DEFAULT_VOICE_ID=os.getenv("DEFAULT_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb"),
            OUTPUT_DIR=Path(os.getenv("OUTPUT_DIRECTORY", "./audio_outputs")),
            VOICE_SAMPLES_DIR=Path("./voice_samples")
        )
    
    def __post_init__(self):
        """Create directories if they don't exist"""
        self.OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
        self.VOICE_SAMPLES_DIR.mkdir(exist_ok=True, parents=True)

config = Config.load()