from llm.gemini import GeminiProvider


llm = GeminiProvider()


def ask_agent(prompt: str) -> str:
    return llm.generate(prompt)