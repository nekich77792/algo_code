"""
Лабораторна робота 19. Завдання 19.2
Задача: "Швидке сортування" (Eolymp #4848, 100%)
https://eolymp.com/uk/problems/4848

Вказівка: Сортування реалізуйте за допомогою алгоритму на базі двійкової купи (heap sort).
"""

import sys


class BinaryMaxHeap:
    """Двійкова максимальна купа для сортування за алгоритмом Heap Sort."""

    def __init__(self, arr: list):
        self._arr = arr
        self._size = len(arr)
        # Побудова максимальної купи за час O(n) (Bottom-up heap construction)
        for i in range((self._size >> 1) - 1, -1, -1):
            self._sift_down(i, self._size)

    def _sift_down(self, idx: int, limit: int) -> None:
        """Просіює елемент униз у межах купи розміром limit."""
        arr = self._arr
        curr_val = arr[idx]
        half = limit >> 1

        while idx < half:
            child = (idx << 1) + 1
            right = child + 1

            if right < limit and arr[right] > arr[child]:
                child = right

            if curr_val >= arr[child]:
                break

            arr[idx] = arr[child]
            idx = child

        arr[idx] = curr_val

    def sort(self) -> list:
        """Пірамідальне сортування (Heap Sort) за час O(n log n) in-place."""
        arr = self._arr
        for end in range(self._size - 1, 0, -1):
            arr[0], arr[end] = arr[end], arr[0]
            self._sift_down(0, end)
        return arr


def solve():
    raw_tokens = sys.stdin.read().split()
    if not raw_tokens:
        return

    data = [int(x) for x in raw_tokens]
    sorted_data = BinaryMaxHeap(data).sort()
    sys.stdout.write(" ".join(str(x) for x in sorted_data) + "\n")


if __name__ == "__main__":
    solve()
