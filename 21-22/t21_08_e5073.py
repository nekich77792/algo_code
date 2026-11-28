"""
Лабораторна робота 21. Завдання 21.8
Задача: "Мультиребра" (Eolymp #5073, 100%)
https://eolymp.com/uk/problems/5073

Алгоритм: Перевірка орієнтованого графа на наявність кратних (повторюваних) дуг.
"""

import sys


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    m = int(tokens[1])
    seen_edges = set()
    it = iter(tokens[2:])
    has_multi = False

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        edge = (u, v)
        if edge in seen_edges:
            has_multi = True
        seen_edges.add(edge)

    sys.stdout.write("YES\n" if has_multi else "NO\n")


if __name__ == "__main__":
    solve()
