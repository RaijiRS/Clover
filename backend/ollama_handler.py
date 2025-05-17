import requests

def generate_response(prompt, context=""):
    full_prompt = f"{context}\nUser: {prompt}\nAssistant:"
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",  # Confirm Ollama port!
            json={"model": "mistral", "prompt": full_prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I couldn't process your request."
