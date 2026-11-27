"""
Лабораторна робота 14. Завдання 14.6
Задача: "Дек необмеженого розміру" (Eolymp #6130, 100%)
https://eolymp.com/uk/problems/6130

Вказівка: Реалізувати дек як рекурсивну структуру.
"""

import sys


class DequeNode:
    """Вузол двозв'язної рекурсивної структури для дека."""

    __slots__ = ("value", "prev", "next")

    def __init__(self, value: int, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node


class RecursiveDeque:
    """Двосторонній дек необмеженого розміру на базі двозв'язного списку."""

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def push_front(self, val: int) -> str:
        """Додає елемент на початок дека."""
        node = DequeNode(val, prev_node=None, next_node=self._front)
        if self._front is None:
            self._front = node
            self._back = node
        else:
            self._front.prev = node
            self._front = node
        self._size += 1
        return "ok"

    def push_back(self, val: int) -> str:
        """Додає елемент у кінець дека."""
        node = DequeNode(val, prev_node=self._back, next_node=None)
        if self._back is None:
            self._front = node
            self._back = node
        else:
            self._back.next = node
            self._back = node
        self._size += 1
        return "ok"

    def pop_front(self) -> str:
        """Вилучає перший елемент або повертає 'error'."""
        if self._front is None:
            return "error"
        val = self._front.value
        self._front = self._front.next
        if self._front is None:
            self._back = None
        else:
            self._front.prev = None
        self._size -= 1
        return str(val)

    def pop_back(self) -> str:
        """Вилучає останній елемент або повертає 'error'."""
        if self._back is None:
            return "error"
        val = self._back.value
        self._back = self._back.prev
        if self._back is None:
            self._front = None
        else:
            self._back.next = None
        self._size -= 1
        return str(val)

    def front(self) -> str:
        """Повертає значення першого елемента або 'error'."""
        if self._front is None:
            return "error"
        return str(self._front.value)

    def back(self) -> str:
        """Повертає значення останнього елемента або 'error'."""
        if self._back is None:
            return "error"
        return str(self._back.value)

    def size(self) -> str:
        """Повертає кількість елементів у деку."""
        return str(self._size)

    def clear(self) -> str:
        """Очищує дек."""
        curr = self._front
        while curr is not None:
            nxt = curr.next
            curr.prev = None
            curr.next = None
            curr = nxt
        self._front = None
        self._back = None
        self._size = 0
        return "ok"


def solve():
    deque = RecursiveDeque()
    output = []

    for line in sys.stdin:
        tokens = line.split()
        if not tokens:
            continue

        cmd = tokens[0]
        if cmd == "push_front":
            output.append(deque.push_front(int(tokens[1])))
        elif cmd == "push_back":
            output.append(deque.push_back(int(tokens[1])))
        elif cmd == "pop_front":
            output.append(deque.pop_front())
        elif cmd == "pop_back":
            output.append(deque.pop_back())
        elif cmd == "front":
            output.append(deque.front())
        elif cmd == "back":
            output.append(deque.back())
        elif cmd == "size":
            output.append(deque.size())
        elif cmd == "clear":
            output.append(deque.clear())
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
