import logging
import threading
from pathlib import Path
from typing import Optional, Union
import pygame
from pydub import AudioSegment
import io

logger = logging.getLogger(__name__)

class AudioManager:
    """Manages audio playback and processing"""
    
    def __init__(self):
        pygame.mixer.init()
        self._current_audio = None
        self._is_playing = False
        
    def play_audio(
        self, 
        audio: Union[bytes, str, Path],
        blocking: bool = True,
        volume: float = 1.0
    ):
        """
        Play audio from bytes or file
        """
        try:
            # Handle different input types
            if isinstance(audio, (str, Path)):
                audio_path = Path(audio)
                if not audio_path.exists():
                    raise FileNotFoundError(f"Audio file not found: {audio_path}")
                pygame.mixer.music.load(str(audio_path))
            elif isinstance(audio, bytes):
                # Load from bytes
                audio_io = io.BytesIO(audio)
                pygame.mixer.music.load(audio_io)
            else:
                raise ValueError("Invalid audio input type")
            
            # Set volume and play
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play()
            
            self._is_playing = True
            logger.info("Playing audio...")
            
            if blocking:
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            else:
                # Non-blocking playback in thread
                thread = threading.Thread(target=self._playback_thread)
                thread.daemon = True
                thread.start()
                
        except Exception as e:
            logger.error(f"Failed to play audio: {e}")
            raise
        finally:
            self._is_playing = False
    
    def _playback_thread(self):
        """Background playback thread"""
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        self._is_playing = False
    
    def stop_playback(self):
        """Stop current audio playback"""
        if self._is_playing:
            pygame.mixer.music.stop()
            self._is_playing = False
            logger.info("Playback stopped")
    
    def pause_playback(self):
        """Pause current playback"""
        if self._is_playing:
            pygame.mixer.music.pause()
            logger.info("Playback paused")
    
    def resume_playback(self):
        """Resume paused playback"""
        pygame.mixer.music.unpause()
        logger.info("Playback resumed")