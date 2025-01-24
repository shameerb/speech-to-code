from setuptools import setup, find_packages

setup(
    name="audio_copilot",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "SpeechRecognition==3.14.0",
        "openai==0.28.0",
        "PyAudio==0.2.14",
        "python-dotenv==1.0.0",
        "standard-aifc==3.13.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A voice-controlled code generation tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
) 