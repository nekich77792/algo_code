"""
Лабораторна робота 14. Завдання 14.5
Задача: "Черга з захистом від помилок" (Eolymp #6126, 100%)
https://eolymp.com/uk/problems/6126

Вказівка: Реалізувати чергу як рекурсивну структуру.
"""

import sys


class QueueNode:
    """Вузол рекурсивної структури черги."""

    __slots__ = ("value", "next")

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next = next_node


class RecursiveQueue:
    """Черга з захистом від помилок на базі однозв'язного ланцюжка вузлів."""

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push(self, val: int) -> str:
        """Додає елемент у кінець черги."""
        node = QueueNode(val)
        if self._back is None:
            self._front = node
            self._back = node
        else:
            self._back.next = node
            self._back = node
        self._size += 1
        return "ok"

    def pop(self) -> str:
        """Вилучає перший елемент або повертає 'error'."""
        if self._front is None:
            return "error"
        val = self._front.value
        self._front = self._front.next
        if self._front is None:
            self._back = None
        self._size -= 1
        return str(val)

    def front(self) -> str:
        """Повертає значення першого елемента без вилучення або 'error'."""
        if self._front is None:
            return "error"
        return str(self._front.value)

    def size(self) -> str:
        """Повертає поточну кількість елементів у черзі."""
        return str(self._size)

    def clear(self) -> str:
        """Очищує чергу."""
        self._front = None
        self._back = None
        self._size = 0
        return "ok"


def solve():
    queue = RecursiveQueue()
    output = []

    for line in sys.stdin:
        tokens = line.split()
        if not tokens:
            continue

        cmd = tokens[0]
        if cmd == "push":
            output.append(queue.push(int(tokens[1])))
        elif cmd == "pop":
            output.append(queue.pop())
        elif cmd == "front":
            output.append(queue.front())
        elif cmd == "size":
            output.append(queue.size())
        elif cmd == "clear":
            output.append(queue.clear())
        elif cmd == "exit":
            output.append("bye")
            break

        if len(output) >= 8192:
            sys.stdout.write("\n".join(output) + "\n")
            output.clear()

    if output:
        sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
