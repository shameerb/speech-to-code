import unittest
from src.core.code_generation import TransformersCodeGeneration

class TestDeepSeekCodeGeneration(unittest.TestCase):
    
    def test_generate_code(self):
        code_generation = TransformersCodeGeneration(model_name = "TheBloke/deepseek-coder-6.7B-base-GGUF")
        text_input = "Create a Python function that returns the square of a number."
        generated_code = code_generation.generate_code(text_input)
        print("Generated Code:\n", generated_code)
        self.assertIn("def", generated_code)
        self.assertIn("return", generated_code)

if __name__ == "__main__":
    unittest.main()