from google import genai

from config import GEMINI_API_KEY
from . import LLMProvider


class GeminiProvider(LLMProvider):

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str, tools=None) -> str:
        config = {}

        if tools:
            config["tools"] = tools

        chat = self.client.chats.create(
            model="gemini-3.6-flash",
            config=config,
        )

        response = chat.send_message(prompt)

        return response.text