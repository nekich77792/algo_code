"""
Лабораторна робота 9. Завдання 9.5
Задача: "Сортування злиттям" (Eolymp #4037, 60%)
https://eolymp.com/uk/problems/4037

Алгоритм: Сортування злиттям (Merge Sort)
"""

import sys

sys.setrecursionlimit(200000)


def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    i = 0
    j = 0
    n1 = len(left)
    n2 = len(right)

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < n1:
        result.extend(left[i:])
    if j < n2:
        result.extend(right[j:])

    return result


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    arr = [int(x) for x in input_data[1:n + 1]]

    sorted_arr = merge_sort(arr)
    sys.stdout.write(" ".join(map(str, sorted_arr)) + "\n")


if __name__ == "__main__":
    solve()
