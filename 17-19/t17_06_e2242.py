"""
Лабораторна робота 17. Завдання 17.6
Задача: "Родовідне дерево" (Eolymp #2242, 100%)
https://eolymp.com/uk/problems/2242

Вказівка 1: У завданні має бути реалізоване та використане бінарне дерево.
Вказівка 2: Дерево має бути реалізоване як рекурсивна структура.
"""

import sys

sys.setrecursionlimit(50000)


class TreeNode:
    """Вузол бінарного дерева пошуку (рекурсивна структура даних)."""

    __slots__ = ("val", "left", "right")

    def __init__(self, val: str, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, new_val: str) -> "TreeNode":
        """Рекурсивно вставляє значення у бінарне дерево пошуку."""
        if new_val < self.val:
            if self.left is None:
                self.left = TreeNode(new_val)
            else:
                self.left.insert(new_val)
        elif new_val > self.val:
            if self.right is None:
                self.right = TreeNode(new_val)
            else:
                self.right.insert(new_val)
        return self

    def preorder(self, out: list) -> None:
        """Рекурсивний прямий обхід (pre-order): корінь -> ліве піддерево -> праве піддерево."""
        out.append(self.val)
        if self.left is not None:
            self.left.preorder(out)
        if self.right is not None:
            self.right.preorder(out)


def solve():
    raw_lines = sys.stdin.read().splitlines()
    if not raw_lines:
        return

    rows = []
    for line in raw_lines:
        trimmed = line.strip()
        if not trimmed:
            continue
        if trimmed in ("*", "$"):
            if rows:
                root = None
                # Відновлюємо дерево від кореня (останній знятий листок) до листків
                for row in reversed(rows):
                    for ch in row:
                        if not ch.isspace():
                            if root is None:
                                root = TreeNode(ch)
                            else:
                                root.insert(ch)

                if root is not None:
                    out = []
                    root.preorder(out)
                    sys.stdout.write("".join(out) + "\n")
                rows = []
            if trimmed == "$":
                break
            continue
        rows.append(trimmed)

    # Якщо вхід завершився без завершального маркера '*'
    if rows:
        root = None
        for row in reversed(rows):
            for ch in row:
                if not ch.isspace():
                    if root is None:
                        root = TreeNode(ch)
                    else:
                        root.insert(ch)

        if root is not None:
            out = []
            root.preorder(out)
            sys.stdout.write("".join(out) + "\n")


if __name__ == "__main__":
    solve()
