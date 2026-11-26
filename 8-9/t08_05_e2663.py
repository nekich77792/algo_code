"""
Лабораторна робота 8. Завдання 8.5
Задача: "Сортування бульбашкою" (Eolymp #2663, 100%)
https://eolymp.com/uk/problems/2663

Алгоритм: Сортування бульбашкою (Bubble Sort)
"""

import sys


def bubble_sort_swaps(arr: list) -> int:
    n = len(arr)
    swaps = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    result = bubble_sort_swaps(arr)
    print(result)


if __name__ == "__main__":
    solve()
