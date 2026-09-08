from llm.router import LLMRouter
from tools import calculate


llm = LLMRouter()


def ask_agent(prompt: str) -> str:
    return llm.generate(
        prompt,
        tools=[calculate],
    )