"""
Лабораторна робота 8. Завдання 8.8
Задача: "Сортування часу" (Eolymp #972, 100%)
https://eolymp.com/uk/problems/972

Алгоритм: Сортування вставкою (Insertion Sort) для кортежів (h, m, s)
"""

import sys


def insertion_sort_time(times: list) -> list:
    n = len(times)
    for i in range(1, n):
        key = times[i]
        j = i - 1
        while j >= 0 and times[j] > key:
            times[j + 1] = times[j]
            j -= 1
        times[j + 1] = key
    return times


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    times = []
    idx = 1
    for _ in range(n):
        h = int(input_data[idx])
        m = int(input_data[idx + 1])
        s = int(input_data[idx + 2])
        times.append((h, m, s))
        idx += 3

    insertion_sort_time(times)

    for h, m, s in times:
        print(f"{h} {m} {s}")


if __name__ == "__main__":
    solve()
