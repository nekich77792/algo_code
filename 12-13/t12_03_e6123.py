"""
Лабораторна робота 12. Завдання 12.3
Задача: "Стек із захистом від помилок" (Eolymp #6123, 100%)
https://eolymp.com/uk/problems/6123

Вказівка: Реалізуйте стек як рекурсивну структуру.
"""

import sys


class LinkedNode:
    """Вузол рекурсивної структури даних стеку."""

    def __init__(self, data: int, next_node=None):
        self.data = data
        self.next = next_node


class RecursiveStack:
    """Стек із захистом від помилок на основі рекурсивної структури (зв'язного списку)."""

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, val: int) -> str:
        """Додає елемент на вершину стеку."""
        self._head = LinkedNode(val, self._head)
        self._size += 1
        return "ok"

    def pop(self) -> str:
        """Вилучає верхній елемент або повертає 'error', якщо стек порожній."""
        if self._head is None:
            return "error"
        val = self._head.data
        self._head = self._head.next
        self._size -= 1
        return str(val)

    def back(self) -> str:
        """Повертає значення верхнього елемента без вилучення або 'error'."""
        if self._head is None:
            return "error"
        return str(self._head.data)

    def size(self) -> str:
        """Повертає поточну кількість елементів у стеку."""
        return str(self._size)

    def clear(self) -> str:
        """Очищує стек."""
        self._head = None
        self._size = 0
        return "ok"


def solve():
    stack = RecursiveStack()
    output = []

    for line in sys.stdin:
        tokens = line.split()
        if not tokens:
            continue

        cmd = tokens[0]
        if cmd == "push":
            output.append(stack.push(int(tokens[1])))
        elif cmd == "pop":
            output.append(stack.pop())
        elif cmd == "back":
            output.append(stack.back())
        elif cmd == "size":
            output.append(stack.size())
        elif cmd == "clear":
            output.append(stack.clear())
        elif cmd == "exit":
            output.append("bye")
            break

    if output:
        sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
