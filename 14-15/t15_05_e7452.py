"""
Лабораторна робота 15. Завдання 15.5
Задача: "Виведення зв’язного списку" (Eolymp #7452, 100%)
https://eolymp.com/uk/problems/7452

Вказівка 1: Реалізувати та використати один з різновидів зв'язного списку (двозв'язний список).
Вказівка 2: Забороняється використовувати масиви (list, tuple тощо) та відображення окрім блоку зчитування.
"""

import sys


class ListNode:
    """Вузол двозв'язного списку."""

    __slots__ = ("data", "prev", "next")

    def __init__(self, data: int, prev_node=None, next_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node


class DoublyLinkedList:
    """Двозв'язний список з вказівниками на head та tail."""

    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val: int) -> None:
        """Додає елемент val у хвіст списку."""
        node = ListNode(val, prev_node=self.tail, next_node=None)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def Print(self) -> None:
        """Виводить елементи списку у прямому порядку (через next)."""
        curr = self.head
        first = True
        while curr is not None:
            if not first:
                sys.stdout.write(" ")
            sys.stdout.write(str(curr.data))
            first = False
            curr = curr.next
        sys.stdout.write("\n")

    def PrintReverse(self) -> None:
        """Виводить елементи списку у зворотному порядку (через prev)."""
        curr = self.tail
        first = True
        while curr is not None:
            if not first:
                sys.stdout.write(" ")
            sys.stdout.write(str(curr.data))
            first = False
            curr = curr.prev
        sys.stdout.write("\n")


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    linked_list = DoublyLinkedList()

    # Заповнюємо зв'язний список даними з вхідного потоку
    for i in range(1, n + 1):
        linked_list.addToTail(int(tokens[i]))

    del tokens  # Звільняємо буфер вхідних токенів

    # Виведення виконується суто через перехід за вказівниками списку
    linked_list.Print()
    linked_list.PrintReverse()


if __name__ == "__main__":
    solve()
