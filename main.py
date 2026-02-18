import os
import argparse
from dotenv import load_dotenv
from google import genai

def get_ai_response(client, prompt):
    response = client.models.generate_content(
        model='gemini-2.5-flash', contents=prompt
    )
    if response.usage_metadata is None:
        raise RuntimeError("API request failed: usage metadata is missing")
    return response

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("api key not found, check .env")

    client = genai.Client(api_key=api_key)

    try:
        response = get_ai_response(client, args.user_prompt)
        
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("-" * 20)
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
