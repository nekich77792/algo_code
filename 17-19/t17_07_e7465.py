"""
Лабораторна робота 17. Завдання 17.7
Задача: "Однакові дерева" (Eolymp #7465, 100%)
https://eolymp.com/uk/problems/7465

Вказівка 1: У завданні має бути реалізоване та використане бінарне дерево.
Вказівка 2: Дерево має бути реалізоване як рекурсивна структура.
"""

import sys

sys.setrecursionlimit(50000)


class TreeNode:
    """Вузол бінарного дерева пошуку (рекурсивна структура даних)."""

    __slots__ = ("val", "left", "right")

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val: int) -> "TreeNode":
        """Рекурсивно вставляє значення у відповідне піддерево."""
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            # Рівні або більші елементи додаються у праве піддерево за правилами задачі
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)
        return self

    def is_same_node(self, other: "TreeNode") -> bool:
        """Рекурсивно перевіряє структурну та змістовну еквівалентність двох піддерев."""
        if other is None:
            return False
        if self.val != other.val:
            return False

        left_equal = (self.left is None and other.left is None) or (
            self.left is not None and self.left.is_same_node(other.left)
        )
        if not left_equal:
            return False

        right_equal = (self.right is None and other.right is None) or (
            self.right is not None and self.right.is_same_node(other.right)
        )
        return right_equal


class BinarySearchTree:
    """Бінарне дерево пошуку."""

    def __init__(self):
        self.root = None

    def insert(self, val: int) -> None:
        """Вставляє значення у дерево."""
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.root.insert(val)

    def is_same(self, other: "BinarySearchTree") -> int:
        """Повертає 1, якщо дерева однакові, інакше 0."""
        if self.root is None and other.root is None:
            return 1
        if self.root is None or other.root is None:
            return 0
        return 1 if self.root.is_same_node(other.root) else 0


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    tree1 = BinarySearchTree()
    for _ in range(n):
        tree1.insert(int(next(it)))

    m = int(next(it))
    tree2 = BinarySearchTree()
    for _ in range(m):
        tree2.insert(int(next(it)))

    result = tree1.is_same(tree2)
    sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    solve()
