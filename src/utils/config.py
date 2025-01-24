import os
from dotenv import load_dotenv

def load_config():
    """Load configuration from environment variables."""
    load_dotenv()
    
    openai_key = os.getenv("OPENAI_API_KEY")
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")
    anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        
    return {
        "openai_key": openai_key,
        "deepseek_key": deepseek_key,
        "anthropic_key": anthropic_key
    } 