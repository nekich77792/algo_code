"""
Лабораторна робота 14. Завдання 14.7
Задача: "Гра у п’яницю" (Eolymp #4005, 90%)
https://eolymp.com/uk/problems/4005

Вказівка: Використати чергу, дек або один із списків.
"""

import sys


class CardNode:
    """Вузол зв'язного списку для моделювання карт у колоді."""

    __slots__ = ("value", "next")

    def __init__(self, value: int):
        self.value = value
        self.next = None


class CardQueue:
    """Черга карт із повторним використанням існуючих вузлів для швидкодії."""

    def __init__(self):
        self._front = None
        self._back = None

    def is_empty(self) -> bool:
        """Перевіряє, чи черга порожня."""
        return self._front is None

    def enqueue(self, val: int) -> None:
        """Створює новий вузол та додає його в хвіст черги."""
        self.enqueue_node(CardNode(val))

    def enqueue_node(self, node: CardNode) -> None:
        """Додає вже існуючий вузол у кінець черги без зайвого виділення пам'яті."""
        node.next = None
        if self._back is None:
            self._front = node
            self._back = node
        else:
            self._back.next = node
            self._back = node

    def dequeue_node(self) -> CardNode:
        """Вилучає перший вузол з голови черги та повертає його."""
        node = self._front
        self._front = node.next
        if self._front is None:
            self._back = None
        return node


def play_drunkard(deck1: CardQueue, deck2: CardQueue, n: int) -> str:
    """
    Моделює гру 'П'яниця' до перемоги або ліміту у 200 000 ходів.
    Правило: карта 0 б'є карту n - 1; в інших випадках перемагає більша.
    """
    max_card = n - 1
    max_turns = 200_000
    turns = 0

    while not deck1.is_empty() and not deck2.is_empty() and turns < max_turns:
        c1_node = deck1.dequeue_node()
        c2_node = deck2.dequeue_node()
        v1 = c1_node.value
        v2 = c2_node.value

        # Визначаємо переможця раунду
        if (v1 == 0 and v2 == max_card) or (v1 > v2 and not (v1 == max_card and v2 == 0)):
            winner = deck1
        else:
            winner = deck2

        # Переможець кладе спочатку карту першого гравця, потім другого
        winner.enqueue_node(c1_node)
        winner.enqueue_node(c2_node)
        turns += 1

    if deck1.is_empty():
        return f"second {turns}"
    if deck2.is_empty():
        return f"first {turns}"
    return "draw"


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    half = n // 2

    deck1 = CardQueue()
    deck2 = CardQueue()

    for i in range(1, half + 1):
        deck1.enqueue(int(tokens[i]))
    for i in range(half + 1, n + 1):
        deck2.enqueue(int(tokens[i]))

    del tokens  # Звільняємо пам'ять списку токенів

    sys.stdout.write(play_drunkard(deck1, deck2, n) + "\n")


if __name__ == "__main__":
    solve()
