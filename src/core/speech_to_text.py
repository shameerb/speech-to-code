from abc import ABC, abstractmethod
import speech_recognition as sr
from typing import Optional

class SpeechToTextStrategy(ABC):
    @abstractmethod
    def recognize_speech(self) -> Optional[str]:
        pass

# Google Speech Recognition online text to speech
class GoogleSpeechToText(SpeechToTextStrategy):
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self) -> Optional[str]:
        try:
            with sr.Microphone() as source:
                print("Listening for code instructions...")
                audio = self.recognizer.listen(source)
                
                print("Converting speech to text...")
                text = self.recognizer.recognize_google(audio)
                return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None 
        
# Offline text to speech (whisper)
class WhisperSpeechToText(SpeechToTextStrategy):
    def __init__(self, model_size="base"):
        self.recognizer = sr.Recognizer()
        self.model_size = model_size

    def recognize_speech(self) -> Optional[str]:
        try:
            with sr.Microphone() as source:
                print("Listening for code instructions...")
                audio = self.recognizer.listen(source)
                
                print("Converting speech to text using Whisper...")
                # Use the specified Whisper model size (tiny, base, small, medium, large)
                text = self.recognizer.recognize_whisper(audio, model=self.model_size)
                return text
        except sr.UnknownValueError:
            print("Could not understand audio") 
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

