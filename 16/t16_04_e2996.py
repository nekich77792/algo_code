"""
Лабораторна робота 16. Завдання 16.4
Задача: "Корупція" (Eolymp #2996, 100%)
https://eolymp.com/uk/problems/2996

Вказівка 1: У завданні має бути реалізоване та використане дерево.
Вказівка 2: Дерево має бути реалізоване як рекурсивна структура.
"""

import sys

# Збільшення ліміту глибини рекурсії для глибоких дерев
sys.setrecursionlimit(50000)


class TreeNode:
    """Вузол дерева підпорядкування співробітників (рекурсивна деревоподібна структура)."""

    def __init__(self, node_id: int, fee: int = 0):
        self.node_id = node_id
        self.fee = fee
        self.children = []

    def add_child(self, child: "TreeNode") -> None:
        """Додає підлеглого співробітника до списку нащадків."""
        self.children.append(child)

    def min_cost(self) -> int:
        """
        Рекурсивно обчислює мінімальну суму офіційних зборів
        від листка (працівника без підлеглих) до поточного вузла.
        """
        if not self.children:
            return self.fee
        best_child_cost = min(child.min_cost() for child in self.children)
        return self.fee + best_child_cost


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))

    # Створюємо вузли для кожного працівника від 1 до n
    nodes = [TreeNode(i) for i in range(n + 1)]

    for emp_id in range(1, n + 1):
        fee = int(next(it))
        k = int(next(it))
        nodes[emp_id].fee = fee
        for _ in range(k):
            subordinate_id = int(next(it))
            nodes[emp_id].add_child(nodes[subordinate_id])

    # Директор організації завжди має номер 1 (корінь дерева)
    result = nodes[1].min_cost()
    sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    solve()
