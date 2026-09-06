from agent import ask_agent


def main():
    response = ask_agent(
        "We sold 125 units at ₹1499 each. "
        "Calculate the total revenue using the calculator tool."
    )

    print(response)


if __name__ == "__main__":
    main()