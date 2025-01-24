from .speech_to_text import SpeechToTextStrategy
from .code_generation import CodeGenerationStrategy

class AudioCopilot:
    def __init__(self, speech_to_text: SpeechToTextStrategy, code_generation: CodeGenerationStrategy):
        self.speech_to_text = speech_to_text
        self.code_generation = code_generation

    def run(self):
        """Main loop for audio code completion."""
        while True:
            text = self.speech_to_text.recognize_speech()
            if text:
                print(f"You said: {text}")
                code = self.code_generation.generate_code(text)
                print("\nGenerated Code:")
                print(code)
                
            user_input = input("\nContinue? (y/n): ")
            if user_input.lower() != 'y':
                break 