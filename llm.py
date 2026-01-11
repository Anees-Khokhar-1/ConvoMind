import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MODEL = "qwen2:0.5b"

def generate_response(prompt: str) -> str:
    try:
        payload = {
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=60
        )
        response.raise_for_status()

        data = response.json()
        return data.get("response", "").strip()

    except Exception as e:
        return f"❌ LLM Error: {str(e)}"
