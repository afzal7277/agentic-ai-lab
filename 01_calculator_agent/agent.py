from google import genai
from google.genai import types

from config import GEMINI_API_KEY
from tools import calculate


client = genai.Client(api_key=GEMINI_API_KEY)


def ask_agent(prompt: str) -> str:
    chat = client.chats.create(
        model="gemini-3.7-flash",
        config=types.GenerateContentConfig(
            tools=[calculate],
            tool_config=types.ToolConfig(
                function_calling_config=types.FunctionCallingConfig(
                    mode="ANY",
                    allowed_function_names=["calculate"],
                )
            ),
        ),
    )

    response = chat.send_message(prompt)

    print("\n--- Agent Response Parts ---")
    for part in response.parts:
        print(part)

    print("----------------------------\n")

    return response.text