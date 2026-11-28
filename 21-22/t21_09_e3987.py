"""
Лабораторна робота 21. Завдання 21.9
Задача: "Повний граф" (Eolymp #3987, 100%)
https://eolymp.com/uk/problems/3987

Алгоритм: Перевірка неорієнтованого графа на повноту (наявність усіх n*(n-1)//2 ребер).
"""

import sys


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])

    unique_edges = set()
    it = iter(tokens[2:])

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u == v:
            continue
        edge = (u, v) if u < v else (v, u)
        unique_edges.add(edge)

    expected_edges = n * (n - 1) // 2
    if len(unique_edges) == expected_edges:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()
