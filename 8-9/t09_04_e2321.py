"""
Лабораторна робота 9. Завдання 9.4
Задача: "Сортування" (Eolymp #2321, 100%)
https://eolymp.com/uk/problems/2321

Алгоритм: Швидке сортування (Quick Sort)
"""

import sys
import random

sys.setrecursionlimit(200000)


def quick_sort(arr: list, low: int = 0, high: int = None):
    if high is None:
        high = len(arr) - 1

    if low >= high:
        return

    pivot_idx = random.randint(low, high)
    pivot = arr[pivot_idx]

    lt = low
    gt = high
    i = low

    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1

    quick_sort(arr, low, lt - 1)
    quick_sort(arr, gt + 1, high)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    quick_sort(arr)
    print(*(arr))


if __name__ == "__main__":
    solve()
