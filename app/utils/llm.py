import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model_name = "gemini-1.5-flash-latest"
generation_config = {
    'temperature': 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

model = genai.GenerativeModel(model_name, generation_config=generation_config)

def ask_gemini(prompt: str) -> str:
    try:
        chat = model.start_chat()
        response = chat.send_message(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Gemini error with {model_name}: {str(e)}")
        print("\nChecking available models:")
        for m in genai.list_models():
            print(f"Model: {m.name}")
            print(f"  Supported methods: {m.supported_generation_methods}")
        return f"Gemini API error ({model_name}): " + str(e)

if __name__ == "__main__":
    while True:
        user_prompt = input("You: ")
        if user_prompt.lower() in ["quit", "exit", "bye"]:
            break
        gemini_response = ask_gemini(user_prompt)
        pass