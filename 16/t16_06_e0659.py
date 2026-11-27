"""
Лабораторна робота 16. Завдання 16.6
Задача: "Дерево гри" (Eolymp #659, 100%)
https://eolymp.com/uk/problems/659

Вказівка 1: У завданні має бути реалізоване та використане дерево.
Вказівка 2: Дерево має бути реалізоване як рекурсивна структура.
"""

import sys

sys.setrecursionlimit(50000)


class GameNode:
    """Вузол дерева гри для двох гравців (рекурсивна структура дерева гри)."""

    def __init__(self, node_id: int, payoff: int = None):
        self.node_id = node_id
        self.payoff = payoff
        self.children = []

    def add_child(self, child: "GameNode") -> None:
        """Додає нащадка (варіант наступного ходу)."""
        self.children.append(child)

    def minimax(self, is_first_player: bool) -> int:
        """
        Рекурсивно обчислює результат гри при оптимальних діях обох гравців
        за допомогою класичного алгоритму мінімакс.
        Перший гравець максимізує результат, другий - мінімізує.
        """
        if self.payoff is not None:
            return self.payoff

        if not self.children:
            return 0

        if is_first_player:
            return max(child.minimax(False) for child in self.children)
        else:
            return min(child.minimax(True) for child in self.children)


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))

    # Створюємо всі вузли гри від 1 до n
    nodes = [GameNode(i) for i in range(n + 1)]

    for node_id in range(2, n + 1):
        node_type = next(it)
        parent_id = int(next(it))

        if node_type == "L":
            payoff_val = int(next(it))
            nodes[node_id].payoff = payoff_val

        nodes[parent_id].add_child(nodes[node_id])

    # Корінь дерева має номер 1, гру розпочинає перший гравець
    result = nodes[1].minimax(is_first_player=True)
    sys.stdout.write(("+1" if result == 1 else str(result)) + "\n")


if __name__ == "__main__":
    solve()
