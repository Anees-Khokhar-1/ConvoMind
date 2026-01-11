# config.py

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
LLM_MODEL = "qwen2:0.5b"
TIMEOUT = 120

MAX_MEMORY_TURNS = 6

SYSTEM_PROMPT = """
You are ConvoMind, a helpful AI assistant.
Answer clearly and concisely.
"""
