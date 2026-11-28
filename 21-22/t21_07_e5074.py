"""
Лабораторна робота 21. Завдання 21.7
Задача: "Степені вершин за списками ребер" (Eolymp #5074, 100%)
https://eolymp.com/uk/problems/5074

Алгоритм: Обчислення степенів вершин неорієнтованого графа за списком ребер.
"""

import sys


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])

    degrees = [0] * (n + 1)
    it = iter(tokens[2:])

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        degrees[u] += 1
        degrees[v] += 1

    output = [str(degrees[v]) for v in range(1, n + 1)]
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
