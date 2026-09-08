from .gemini import GeminiProvider
from .groq import GroqProvider


class LLMRouter:

    def __init__(self, force_gemini_failure=False):
        self.gemini = GeminiProvider()
        self.groq = GroqProvider()
        self.force_gemini_failure = force_gemini_failure

    def generate(self, prompt: str, tools=None) -> str:

        try:
            print("Using Gemini...")

            if self.force_gemini_failure:
                raise RuntimeError("Intentional Gemini failure for fallback testing")

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