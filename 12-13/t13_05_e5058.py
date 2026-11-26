"""
Лабораторна робота 13. Завдання 13.5
Задача: "Дужкова послідовність" (Eolymp #5058, 100%)
https://eolymp.com/uk/problems/5058

Алгоритм: Перевірка правильності дужкової структури за допомогою стеку
"""

import sys


def is_valid_brackets(seq: str) -> bool:
    """
    Перевіряє правильність дужкової послідовності, що містить
    символи '()', '[]', '{}', використовуючи стек.
    """
    stack = []
    matching = {")": "(", "]": "[", "}": "{"}

    for ch in seq:
        if ch in "([{":
            stack.append(ch)
        elif ch in matching:
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def solve():
    line = sys.stdin.read().strip()
    if is_valid_brackets(line):
        sys.stdout.write("yes\n")
    else:
        sys.stdout.write("no\n")


if __name__ == "__main__":
    solve()
