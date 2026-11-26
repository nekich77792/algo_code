"""
Лабораторна робота 12. Завдання 12.4
Задача: "Рейки" (Eolymp #1776, 100%)
https://eolymp.com/uk/problems/1776

Алгоритм: Моделювання залізничного тупика за допомогою стеку (LIFO)
"""

import sys


def can_form_train(n: int, target: list) -> bool:
    """
    Перевіряє за допомогою стеку, чи можна переставити вагони
    з початкового порядку 1..n у цільовий порядок target.
    """
    station_stack = []
    incoming_car = 1

    for needed_car in target:
        # Заганяємо вагони у тупик, доки на вершині не опиниться потрібний вагон
        while incoming_car <= n and (not station_stack or station_stack[-1] != needed_car):
            station_stack.append(incoming_car)
            incoming_car += 1

        # Якщо на вершині тупика потрібний вагон — відправляємо його у напрямок B
        if station_stack and station_stack[-1] == needed_car:
            station_stack.pop()
        else:
            return False

    return True


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    output = []

    while True:
        try:
            n_str = next(it)
        except StopIteration:
            break

        n = int(n_str)
        if n == 0:
            break

        # Обробляємо всі тестові перестановки для поточного N
        while True:
            first_val = int(next(it))
            if first_val == 0:
                output.append("")  # Порожній рядок між блоками
                break

            target = [first_val] + [int(next(it)) for _ in range(n - 1)]
            output.append("Yes" if can_form_train(n, target) else "No")

    if output:
        sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
