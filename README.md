## Audio copilot
Convert speech to code. Interact with your codebase using speech models.

## Notes/Thoughts for Design
- [VsCode](https://code.visualstudio.com/docs/editor/voice) already supports audio prompts (command + I)
- The prompt to code part is already being done efficiently using editors like cursor, zed, void.
- Use speech prompts to generate, edit, debug etc
- Speech to text model should be low latency, accurate and light weight (low compute) to be run on any local machine
- The code generation part is already supported by existing editors.

## Resources
- Existing features
    - https://code.visualstudio.com/docs/editor/voice
    - https://githubnext.com/projects/copilot-voice/
- Speech to text
    - https://platform.openai.com/docs/guides/speech-to-text
    - Google Speech Recognition
    - whisper

- Code Generator models
    - https://github.com/deepseek-ai/DeepSeek-Coder
    - anthropic models
    - openai models

- Open source code editors
    - https://voideditor.com/
        - open source alternative to cursor, fork of vscode
    - https://zed.dev/
        - open source, similiar to sublime with copilot support, rust
    - vscode