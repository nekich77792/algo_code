"""
Лабораторна робота 13. Завдання 13.6
Задача: "З префіксного у інфіксне" (Eolymp #731, 100%)
https://eolymp.com/uk/problems/731

Алгоритм: Перетворення префіксного виразу в інфіксний з мінімальними дужками за допомогою стеку
"""

import sys


def prefix_to_infix(expr: str) -> str:
    """
    Перетворює вираз із префіксної форми в інфіксну форму,
    розставляючи дужки лише там, де це необхідно згідно з пріоритетом
    та асоціативністю операцій.
    """
    # Пріоритети: + та - мають 1, * та / мають 2, операнди мають 3
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []  # Елементи: (infix_str, op_precedence)

    # Обходимо вираз справа наліво
    for token in reversed(expr):
        if token in precedence:
            op_prec = precedence[token]
            left_expr, left_prec = stack.pop()
            right_expr, right_prec = stack.pop()

            # Лівий операнд потребує дужок, якщо його пріоритет строго нижчий
            if left_prec < op_prec:
                left_expr = f"({left_expr})"

            # Правий операнд потребує дужок, якщо пріоритет нижчий,
            # або рівний для некомутативних операцій '-' і '/'
            if right_prec < op_prec or (right_prec == op_prec and token in "-/"):
                right_expr = f"({right_expr})"

            stack.append((f"{left_expr}{token}{right_expr}", op_prec))
        else:
            # Операнд має найвищий пріоритет (не потребує власних дужок)
            stack.append((token, 3))

    return stack[-1][0] if stack else ""


def solve():
    raw_input = sys.stdin.read().split()
    if not raw_input:
        return

    expr = "".join(raw_input)
    sys.stdout.write(prefix_to_infix(expr) + "\n")


if __name__ == "__main__":
    solve()
