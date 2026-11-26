"""
Лабораторна робота 8. Завдання 8.7
Задача: "Бібліотечний метод" (Eolymp #2664, 100%)
https://eolymp.com/uk/problems/2664

Алгоритм: Сортування вставкою (Insertion Sort)
"""

import sys


def insertion_sort(arr: list):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        moved = False

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            moved = True

        arr[j + 1] = key

        if moved:
            print(*(arr))


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    insertion_sort(arr)


if __name__ == "__main__":
    solve()
