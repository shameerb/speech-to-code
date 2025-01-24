from abc import ABC, abstractmethod
import openai

# Interface for Code Generation
class CodeGenerationStrategy(ABC):
    @abstractmethod
    def generate_code(self, prompt: str) -> str:
        pass

# Concrete implementation using OpenAI
class OpenAICodeGeneration(CodeGenerationStrategy):
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_code(self, prompt: str) -> str:
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo",
                prompt=f"Write Python code for: {prompt}",
                max_tokens=500,
                temperature=0.7,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error getting code completion: {e}")
            return "" 
        
# Concrete implementation using DeepSeek
class DeepSeekCodeGeneration(CodeGenerationStrategy):
    def __init__(self, api_key: str):
        self.api_key = api_key

    def generate_code(self, prompt: str) -> str:
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # TODO: Replace with actual DeepSeek API endpoint and request format
            response = {
                "code": "# Placeholder for DeepSeek generated code\n"
                        "print('DeepSeek implementation pending')"
            }
            
            return response["code"].strip()
        except Exception as e:
            print(f"Error getting code completion from DeepSeek: {e}")
            return ""

