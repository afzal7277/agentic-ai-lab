from llm.gemini import GeminiProvider
from llm.groq import GroqProvider


def test_provider(name, provider):
    print(f"\n--- Testing {name} ---")

    response = provider.generate(
        "Explain what an AI agent is in one simple sentence."
    )

    print(response)


def main():
    test_provider("Gemini", GeminiProvider())
    test_provider("Groq", GroqProvider())


if __name__ == "__main__":
    main()