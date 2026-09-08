import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def calculate(expression: str) -> float:
    """Safely calculate a mathematical expression."""

    print(f"[TOOL CALL] calculate({expression})")

    try:
        tree = ast.parse(expression, mode="eval")
        result = _evaluate(tree.body)

    except (SyntaxError, ValueError, TypeError, ZeroDivisionError, OverflowError) as error:
        raise ValueError(f"Invalid mathematical expression: {expression}") from error

    print(f"[TOOL RESULT] {result}")

    return result


def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
        operand = _evaluate(node.operand)
        return OPERATORS[type(node.op)](operand)

    if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
        left = _evaluate(node.left)
        right = _evaluate(node.right)

        return OPERATORS[type(node.op)](left, right)

    raise ValueError("Only mathematical expressions are allowed.")