"""
Лабораторна робота 10. Завдання 10.4
Задача: "Перестановки n по k" (Eolymp #9961, 100%)
https://eolymp.com/uk/problems/9961

Алгоритм: Повний перебір / рекурсивний бектрекінг (генерація розміщень n по k)
"""

import sys


def generate_permutations(n: int, k: int):
    used = [False] * (n + 1)
    current = []
    lines = []

    def backtrack(depth: int):
        if depth == k:
            lines.append(" ".join(str(x) for x in current))
            return

        for i in range(1, n + 1):
            if not used[i]:
                used[i] = True
                current.append(i)
                backtrack(depth + 1)
                current.pop()
                used[i] = False

    backtrack(0)
    return "\n".join(lines)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])

    result = generate_permutations(n, k)
    if result:
        sys.stdout.write(result + "\n")


if __name__ == "__main__":
    solve()
