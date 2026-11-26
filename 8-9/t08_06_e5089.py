"""
Лабораторна робота 8. Завдання 8.6
Задача: "Словник" (Eolymp #5089, 100%)
https://eolymp.com/uk/problems/5089

Алгоритм: Сортування вибором (Selection Sort) для рядків
"""

import sys


def selection_sort_strings(words: list) -> list:
    n = len(words)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if words[j] < words[min_idx]:
                min_idx = j
        if min_idx != i:
            words[i], words[min_idx] = words[min_idx], words[i]
    return words


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    words = input_data[1:n + 1]

    selection_sort_strings(words)

    for w in words:
        print(w)


if __name__ == "__main__":
    solve()
