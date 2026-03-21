import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function

def get_ai_response(client, prompt):
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )
    if response.usage_metadata is None:
        raise RuntimeError("API request failed: usage metadata is missing")
    return response

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("api key not found, check .env")

    client = genai.Client(api_key=api_key)
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    for _ in range(20):
        try:
            response = get_ai_response(client, messages)
            if response.candidates:
                for candidate in response.candidates:
                    messages.append(candidate.content)
            
            if args.verbose:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
                print("-" * 20)
            if response.function_calls:
                function_responses = []
                for function_call in response.function_calls:
                    print(f"Calling function: {function_call.name}({function_call.args})")
                    function_call_result = call_function(function_call, verbose=True)
                    if (
                        not function_call_result.parts
                        or not function_call_result.parts[0].function_response
                        or not function_call_result.parts[0].function_response.response
                    ):
                        raise RuntimeError(f"Empty function response for {function_call.name}")
                    if args.verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                    function_responses.append(function_call_result.parts[0])

            if not response.function_calls:
                print(response.text)
                return
            messages.append(types.Content(role="user", parts=function_responses))
        except Exception as e:
            print(f"An error occurred: {e}")
    if _ == 20:
        sys.exit("messages limit reached")

if __name__ == "__main__":
    main()
