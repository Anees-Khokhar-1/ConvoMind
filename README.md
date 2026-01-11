# ConvoMind 🤖

A lightweight local AI chatbot built with Flask and Ollama.

## Features
- Local LLM via Ollama (qwen2 / tinyllama)
- Flask backend
- Simple web chat UI
- Session-based conversation memory
- Offline & private

## Requirements
- Python 3.10+
- Ollama (installed system-wide)
- qwen2:0.5b model

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/ConvoMind.git
cd ConvoMind
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
