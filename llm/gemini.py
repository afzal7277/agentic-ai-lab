from google import genai

from config import GEMINI_API_KEY
from . import LLMProvider


class GeminiProvider(LLMProvider):

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
        )

        return response.text