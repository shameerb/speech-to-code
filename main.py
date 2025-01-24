from src.core import code_generation
from src.core.speech_to_text import GoogleSpeechToText, WhisperSpeechToText
from src.core.code_generation import OpenAICodeGeneration, DeepSeekCodeGeneration, ClaudeCodeGeneration, TransformersCodeGeneration
from src.utils.config import load_config
from src import AudioCopilot

def main():
    config = load_config()
    speech_to_text = GoogleSpeechToText()
    # speech_to_text = WhisperSpeechToText()
    code_generation = OpenAICodeGeneration(config["openai_key"])
    # code_generation = DeepSeekCodeGeneration(config["deepseek_key"] )
    # code_generation = ClaudeCodeGeneration(config["anthropic_key"])
    # code_generation = TransformersCodeGeneration()
    copilot = AudioCopilot(speech_to_text, code_generation)
    copilot.run()

if __name__ == "__main__":
    main() 