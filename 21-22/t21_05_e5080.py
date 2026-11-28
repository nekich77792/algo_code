"""
Лабораторна робота 21. Завдання 21.5
Задача: "Кількість висячих вершин 1" (Eolymp #5080, 100%)
https://eolymp.com/uk/problems/5080

Алгоритм: Підрахунок висячих вершин (степінь = 1) за матрицею суміжності.
"""

import sys


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    it = iter(tokens[1:])
    pendant_count = 0

    for _ in range(n):
        degree = 0
        for _ in range(n):
            if next(it) != "0":
                degree += 1
        if degree == 1:
            pendant_count += 1

    sys.stdout.write(str(pendant_count) + "\n")


if __name__ == "__main__":
    solve()
