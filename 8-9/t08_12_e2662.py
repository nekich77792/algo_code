"""
Лабораторна робота 8. Завдання 8.12
Задача: "Метод мінімуму" (Eolymp #2662, 100%)
https://eolymp.com/uk/problems/2662

Алгоритм: Сортування вибором (Selection Sort)
"""

import sys


def selection_sort_first_moves(arr: list) -> int:
    n = len(arr)
    if n <= 1:
        return 0

    first_val = arr[0]
    moves = 0

    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            if arr[i] == first_val or arr[min_idx] == first_val:
                moves += 1
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return moves


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    result = selection_sort_first_moves(arr)
    print(result)


if __name__ == "__main__":
    solve()
