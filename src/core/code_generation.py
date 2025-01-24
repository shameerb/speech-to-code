from abc import ABC, abstractmethod
import openai
import anthropic
import requests
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


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
        
class ClaudeCodeGeneration(CodeGenerationStrategy):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = anthropic.Anthropic()

    def generate_code(self, prompt: str) -> str:
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20240620",
                max_tokens=1024,
                messages=[
                    {"role": "user", "content": f"Write Python code for: {prompt}"}
                ]
            )
            return response.content[0].text.strip()
        except Exception as e:
            print(f"Error getting code completion from Claude: {e}")
            return ""

# Concrete implementation using DeepSeek
class DeepSeekCodeGeneration(CodeGenerationStrategy):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.deepseek.com/v1/chat/completions"

    def generate_code(self, prompt: str) -> str:
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant"},
                    {"role": "user", "content": f"Write Python code for: {prompt}"}
                ],
                "stream": False
            }
            
            response = requests.post(
                self.base_url,
                headers=headers,
                json=data
            )
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"].strip()
            
        except Exception as e:
            print(f"Error getting code completion: {e}")
            return ""

# Concrete implementation using Transformers
class TransformersCodeGeneration(CodeGenerationStrategy):
    def __init__(self, model_name: str = "bigcode/starcoder"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        if torch.cuda.is_available():
            self.model = self.model.to("cuda")
        
    def generate_code(self, prompt: str) -> str:
        try:
            inputs = self.tokenizer.encode(f"Write Python code for: {prompt}", 
                                         return_tensors="pt")
            if torch.cuda.is_available():
                inputs = inputs.to("cuda")
                
            outputs = self.model.generate(
                inputs,
                max_length=512,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )
            
            generated_code = self.tokenizer.decode(outputs[0], 
                                                 skip_special_tokens=True)
            return generated_code.strip()
            
        except Exception as e:
            print(f"Error generating code with transformers: {e}")
            return ""
