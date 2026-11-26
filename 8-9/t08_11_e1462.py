"""
Лабораторна робота 8. Завдання 8.11
Задача: "Хитре сортування" (Eolymp #1462)
https://eolymp.com/uk/problems/1462

Алгоритм: Сортування вставками (Insertion Sort)
"""

import sys


def is_less(a: int, b: int) -> bool:
    last_a = a % 10
    last_b = b % 10
    if last_a != last_b:
        return last_a < last_b
    return a < b


def tricky_sort(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and is_less(key, arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    tricky_sort(arr)
    print(*(arr))


if __name__ == "__main__":
    solve()
