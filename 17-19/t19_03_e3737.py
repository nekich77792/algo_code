"""
Лабораторна робота 19. Завдання 19.3
Задача: "Куча чи ні?" (Eolymp #3737, 100%)
https://eolymp.com/uk/problems/3737

Зауваження: Вимоги до алгоритму виконання задачі відсутні.
"""

import sys


def is_min_heap(arr: list, n: int) -> bool:
    """
    Перевіряє, чи задовольняє 1-індексований масив розміру n
    властивість мінімальної двійкової купи:
    A[i] <= A[2i] та A[i] <= A[2i + 1] для всіх допустимих i.
    """
    for i in range(1, (n >> 1) + 1):
        left = i << 1
        if left <= n and arr[i] > arr[left]:
            return False

        right = left + 1
        if right <= n and arr[i] > arr[right]:
            return False

    return True


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    # Створюємо 1-індексований масив із фіктивним нульовим елементом
    arr = [0] + [int(x) for x in tokens[1:n + 1]]

    if is_min_heap(arr, n):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    solve()
