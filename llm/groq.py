from groq import Groq

from config import GROQ_API_KEY
from . import LLMProvider


class GroqProvider(LLMProvider):

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate(self, prompt: str, tools=None) -> str:
        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response.choices[0].message.content