import logging
import sys
import io
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich.panel import Panel
from rich.progress import track
import time
import codecs

from config import config
from tts_engine import TTSEngine
from audio_manager import AudioManager

# Setup logging with UTF-8 encoding
def setup_logging():
    """Setup logging with proper encoding for Windows"""
    # Create formatters and handlers
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # File handler with UTF-8 encoding
    file_handler = logging.FileHandler('tts_system.log', encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # Console handler with UTF-8 encoding
    console_handler = logging.StreamHandler(
        codecs.getwriter('utf-8')(sys.stdout.buffer)
    )
    console_handler.setFormatter(formatter)
    
    # Configure root logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logging()
console = Console()

class TTSApplication:
    """Main TTS application - Simplified version"""
    
    def __init__(self):
        self.tts_engine = TTSEngine()
        self.audio_manager = AudioManager()
        self.current_voice_id = config.DEFAULT_VOICE_ID
        
    def run(self):
        """Run the main application loop"""
        console.print(Panel.fit(
            "[bold cyan]🎙️ ElevenLabs TTS System[/bold cyan]\n"
            "Simple Text-to-Speech Converter",
            border_style="cyan"
        ))
        
        while True:
            self.show_menu()
    
    def show_menu(self):
        """Display main menu"""
        console.print("\n[bold]Main Menu:[/bold]")
        options = [
            "1. Quick TTS (Text to Speech)",
            "2. Batch Convert Texts",
            "3. Test Voice Quality",
            "4. Exit"
        ]
        
        for option in options:
            console.print(f"  {option}")
        
        choice = Prompt.ask("\n[cyan]Select option[/cyan]", choices=["1","2","3","4"])
        
        actions = {
            "1": self.quick_tts,
            "2": self.batch_convert,
            "3": self.test_voice,
            "4": self.exit_app
        }
        
        actions[choice]()
    
    def quick_tts(self):
        """Quick text-to-speech conversion"""
        console.print("\n[bold]Quick TTS[/bold]")
        
        text = Prompt.ask("[cyan]Enter text to convert[/cyan]")
        
        if not text:
            console.print("[red]No text provided![/red]")
            return
        
        try:
            # Show progress
            with console.status("[cyan]Converting text to speech...[/cyan]"):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = config.OUTPUT_DIR / f"tts_{timestamp}.mp3"
                
                audio = self.tts_engine.convert_text_to_speech(
                    text=text,
                    voice_id=self.current_voice_id,
                    output_path=output_path
                )
            
            console.print(f"[green]✅ Audio saved to: {output_path}[/green]")
            
            # Play audio
            if Confirm.ask("Play audio now?", default=True):
                self.audio_manager.play_audio(audio)
                
        except Exception as e:
            console.print(f"[red]❌ Error: {e}[/red]")
            logger.error(f"Quick TTS failed: {e}")
    
    def batch_convert(self):
        """Convert multiple texts"""
        console.print("\n[bold]Batch Text Conversion[/bold]")
        
        texts = []
        console.print("[cyan]Enter texts (empty line to finish):[/cyan]")
        
        while True:
            text = input(f"Text {len(texts) + 1}: ")
            if not text:
                break
            texts.append(text)
        
        if not texts:
            console.print("[yellow]No texts provided[/yellow]")
            return
        
        console.print(f"\n[cyan]Converting {len(texts)} texts...[/cyan]")
        
        for i, text in enumerate(track(texts, description="Converting...")):
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = config.OUTPUT_DIR / f"batch_{timestamp}_{i+1}.mp3"
                
                self.tts_engine.convert_text_to_speech(
                    text=text,
                    voice_id=self.current_voice_id,
                    output_path=output_path
                )
                
            except Exception as e:
                console.print(f"[red]Failed text {i+1}: {e}[/red]")
                logger.error(f"Batch convert failed for text {i+1}: {e}")
        
        console.print("[green]✅ Batch conversion complete![/green]")
    
    def test_voice(self):
        """Test voice quality with different settings"""
        console.print("\n[bold]Voice Quality Test[/bold]")
        
        test_text = "This is a test of the voice quality with different settings."
        
        settings_variations = [
            {"stability": 0.3, "similarity_boost": 0.9, "name": "High Similarity"},
            {"stability": 0.7, "similarity_boost": 0.5, "name": "Balanced"},
            {"stability": 0.9, "similarity_boost": 0.3, "name": "High Stability"},
        ]
        
        console.print(f"[cyan]Using voice ID: {self.current_voice_id}[/cyan]\n")
        
        for settings in settings_variations:
            console.print(f"\n[cyan]Testing: {settings['name']}[/cyan]")
            
            try:
                # Create voice settings dict
                voice_settings = {
                    "stability": settings["stability"],
                    "similarity_boost": settings["similarity_boost"]
                }
                
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = config.OUTPUT_DIR / f"test_{settings['name'].replace(' ', '_')}_{timestamp}.mp3"
                
                audio = self.tts_engine.convert_text_to_speech(
                    text=test_text,
                    voice_id=self.current_voice_id,
                    output_path=output_path,
                    voice_settings=voice_settings
                )
                
                console.print(f"  Stability: {settings['stability']}")
                console.print(f"  Similarity: {settings['similarity_boost']}")
                console.print(f"  Saved to: {output_path.name}")
                
                if Confirm.ask("  Play this version?", default=True):
                    self.audio_manager.play_audio(audio)
                
                time.sleep(1)
                
            except Exception as e:
                console.print(f"[red]Test failed: {e}[/red]")
                logger.error(f"Voice test failed: {e}")
    
    def exit_app(self):
        """Exit application"""
        console.print("\n[cyan]Thank you for using ElevenLabs TTS System![/cyan]")
        sys.exit(0)

def main():
    """Entry point"""
    try:
        app = TTSApplication()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]Interrupted by user[/yellow]")
    except Exception as e:
        console.print(f"[red]Fatal error: {e}[/red]")
        logger.exception("Fatal error")
        sys.exit(1)

if __name__ == "__main__":
    main()