from agent import ask_agent


def main():
    response = ask_agent(
        "Explain what an AI agent is in one simple sentence."
    )

    print(response)


if __name__ == "__main__":
    main()