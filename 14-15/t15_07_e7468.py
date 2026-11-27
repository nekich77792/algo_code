"""
Лабораторна робота 15. Завдання 15.7
Задача: "Зміна порядку списку" (Eolymp #7468, 100%)
https://eolymp.com/uk/problems/7468

Вказівка 1: Реалізувати та використати однозв'язний список.
Вказівка 2: Забороняється використовувати будь-який масив (list, tuple тощо) окрім блоку зчитування.
"""

import sys


class ListNode:
    """Вузол однозв'язного списку."""

    __slots__ = ("data", "next")

    def __init__(self, data: int, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    """Однозв'язний список з підтримкою додавання в хвіст та зміни порядку елементів."""

    def __init__(self):
        self.head = None
        self.tail = None

    def addToTail(self, val: int) -> None:
        """Додає значення val у кінець списку."""
        node = ListNode(val)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def ReorderList(self) -> None:
        """
        Переставляє вузли у порядку L0 -> Ln -> L1 -> L(n-1) -> L2 -> ...
        Операція виконується виключно за рахунок зміни вказівників (in-place),
        без створення додаткових масивів чи вузлів.
        """
        if self.head is None or self.head.next is None or self.head.next.next is None:
            return

        # 1. Знаходимо середину списку за допомогою повільного та швидкого вказівників
        slow = self.head
        fast = self.head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None  # Розрізаємо список на дві частини

        # 2. Розвертаємо другу половину списку (in-place)
        prev_node = None
        curr = second_half
        while curr is not None:
            nxt = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = nxt
        second_half = prev_node

        # 3. Почергово зливаємо вузли першої та розвернутої другої половини
        first_half = self.head
        new_tail = first_half
        while second_half is not None:
            next_first = first_half.next
            next_second = second_half.next

            first_half.next = second_half
            second_half.next = next_first
            new_tail = second_half if next_first is None else next_first

            first_half = next_first
            second_half = next_second

        self.tail = new_tail

    def Print(self) -> None:
        """Виводить елементи списку через пробіл виключно обходом по посиланнях next."""
        curr = self.head
        first = True
        while curr is not None:
            if not first:
                sys.stdout.write(" ")
            sys.stdout.write(str(curr.data))
            first = False
            curr = curr.next
        sys.stdout.write("\n")


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    linked_list = LinkedList()

    for i in range(1, n + 1):
        linked_list.addToTail(int(tokens[i]))

    del tokens  # Звільняємо буфер списку вхідних токенів

    # Всі перестановки та виведення виконуються виключно зв'язним списком
    linked_list.ReorderList()
    linked_list.Print()


if __name__ == "__main__":
    solve()
