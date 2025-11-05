import logging
import time
from pathlib import Path
from typing import Optional, Generator, Union
import requests
from elevenlabs.client import ElevenLabs
from elevenlabs import VoiceSettings, stream
from config import config

logger = logging.getLogger(__name__)

class TTSEngine:
    """Main TTS engine for text-to-speech conversion"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or config.API_KEY
        self.client = ElevenLabs(api_key=self.api_key)
        self.session = requests.Session()
        self.session.headers.update({
            "xi-api-key": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
    
    def convert_text_to_speech(
        self,
        text: str,
        voice_id: str = None,
        model_id: str = None,
        voice_settings: Optional[VoiceSettings] = None,
        output_path: Optional[Path] = None,
        stream_audio: bool = False
    ) -> Union[bytes, Generator]:
        """
        Convert text to speech using ElevenLabs API
        """
        if not text:
            raise ValueError("Text cannot be empty")
        
        voice_id = voice_id or config.DEFAULT_VOICE_ID
        model_id = model_id or config.DEFAULT_MODEL
        
        # Default voice settings
        if not voice_settings:
            voice_settings = VoiceSettings(
                stability=config.DEFAULT_STABILITY,
                similarity_boost=config.DEFAULT_SIMILARITY,
                style=config.DEFAULT_STYLE,
                use_speaker_boost=config.USE_SPEAKER_BOOST
            )
        
        try:
            start_time = time.time()
            
            if stream_audio:
                # Stream audio chunks
                logger.info("Streaming audio...")
                audio_stream = self.client.generate(
                    text=text,
                    voice=voice_id,
                    model=model_id,
                    voice_settings=voice_settings,
                    stream=True
                )
                return audio_stream
            else:
                # Get complete audio
                logger.info(f"Converting text ({len(text)} chars) with voice {voice_id}")
                audio = self.client.generate(
                    text=text,
                    voice=voice_id,
                    model=model_id,
                    voice_settings=voice_settings,
                    output_format=config.OUTPUT_FORMAT
                )
                
                # Convert generator to bytes if needed
                if hasattr(audio, '__iter__'):
                    audio = b''.join(audio)
                
                elapsed = time.time() - start_time
                logger.info(f"Audio generated successfully in {elapsed:.2f}s")
                
                # Save to file if path provided
                if output_path:
                    self._save_audio(audio, output_path)
                
                return audio
                
        except Exception as e:
            logger.error(f"TTS conversion failed: {e}")
            raise
    
    def _save_audio(self, audio_data: bytes, output_path: Path):
        """Save audio data to file"""
        try:
            output_path = Path(output_path)
            output_path.parent.mkdir(exist_ok=True, parents=True)
            
            with open(output_path, 'wb') as f:
                f.write(audio_data)
            
            logger.info(f"Audio saved to {output_path}")
        except Exception as e:
            logger.error(f"Failed to save audio: {e}")
            raise
    
    def get_user_info(self) -> dict:
        """Get user subscription info"""
        try:
            # Use the ElevenLabs client to get user info
            user = self.client.user.get()
            return {
                "email": getattr(user, 'email', 'N/A'),
                "character_count": getattr(user.subscription, 'character_count', 0),
                "character_limit": getattr(user.subscription, 'character_limit', 0),
                "can_extend_character_limit": getattr(user.subscription, 'can_extend_character_limit', False),
                "allowed_to_extend_character_limit": getattr(user.subscription, 'allowed_to_extend_character_limit', False),
                "next_character_count_reset_unix": getattr(user.subscription, 'next_character_count_reset_unix', 0),
                "voice_limit": getattr(user.subscription, 'voice_limit', 0),
                "professional_voice_limit": getattr(user.subscription, 'professional_voice_limit', 0),
                "can_use_instant_voice_cloning": getattr(user.subscription, 'can_use_instant_voice_cloning', False),
                "tier": getattr(user.subscription, 'tier', 'free')
            }
        except Exception as e:
            logger.error(f"Failed to get user info: {e}")
            return {}