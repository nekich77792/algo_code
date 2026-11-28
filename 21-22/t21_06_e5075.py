"""
Лабораторна робота 21. Завдання 21.6
Задача: "Півстепені вершин за списками ребер" (Eolymp #5075, 100%)
https://eolymp.com/uk/problems/5075

Алгоритм: Обчислення напівстепенів заходу (in-degree) та виходу (out-degree) орієнтованого графа.
"""

import sys


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    m = int(tokens[1])

    in_degree = [0] * (n + 1)
    out_degree = [0] * (n + 1)

    it = iter(tokens[2:])
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        out_degree[u] += 1
        in_degree[v] += 1

    output = [f"{in_degree[v]} {out_degree[v]}" for v in range(1, n + 1)]
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
