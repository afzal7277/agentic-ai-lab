from .gemini import GeminiProvider
from .groq import GroqProvider


class LLMRouter:

    def __init__(self):
        self.gemini = GeminiProvider()
        self.groq = GroqProvider()

    def generate(self, prompt: str, tools=None) -> str:

        try:
            print("Using Gemini...")

            return self.gemini.generate(
                prompt,
                tools=tools,
            )

        except Exception as e:
            print(f"Gemini failed: {e}")
            print("Falling back to Groq...")

            try:
                return self.groq.generate(
                    prompt,
                    tools=tools,
                )

            except Exception as groq_error:
                raise RuntimeError(
                    f"Both LLM providers failed.\n"
                    f"Gemini error: {e}\n"
                    f"Groq error: {groq_error}"
                )