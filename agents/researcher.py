# Agent 1: Researcher (sempre comprimido)
from llm_workspace import CompressedLLM

agent = CompressedLLM('ollama')
# Comunicação interna: comprimido
# Output para usuário: EXPAND: quando solicitado
