def calculate(expression: str) -> float:
    """Calculate a mathematical expression."""
    print(f"[TOOL CALL] calculate({expression})")

    result = eval(expression)

    print(f"[TOOL RESULT] {result}")

    return result