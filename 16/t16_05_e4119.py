"""
Лабораторна робота 16. Завдання 16.5
Задача: "Дискове дерево" (Eolymp #4119, 100%)
https://eolymp.com/uk/problems/4119

Вказівка 1: У завданні має бути реалізоване та використане дерево.
Вказівка 2: Дерево має бути реалізоване як рекурсивна структура.
"""

import sys

sys.setrecursionlimit(50000)


class DirNode:
    """Вузол дерева каталогів (рекурсивна деревоподібна структура)."""

    __slots__ = ("name", "children")

    def __init__(self, name: str = ""):
        self.name = name
        self.children = None

    def get_or_create_child(self, child_name: str) -> "DirNode":
        """Повертає існуючий дочірній вузол або створює новий."""
        if self.children is None:
            self.children = []

        for child in self.children:
            if child.name == child_name:
                return child

        new_child = DirNode(child_name)
        self.children.append(new_child)
        return new_child

    def insert_path(self, path_components: list, index: int = 0) -> None:
        """Рекурсивно вставляє компоненти шляху до дерева каталогів."""
        if index >= len(path_components):
            return

        child = self.get_or_create_child(path_components[index])
        child.insert_path(path_components, index + 1)

    def print_tree(self, depth: int = -1) -> None:
        """
        Рекурсивно виводить дерево каталогів з відступами відповідно до глибини.
        Підкаталоги в межах одного каталогу сортуються лексикографічно.
        """
        if depth >= 0:
            sys.stdout.write(" " * depth + self.name + "\n")

        if self.children is None:
            return

        self.children.sort(key=lambda node: node.name)
        for child in self.children:
            child.print_tree(depth + 1)


def solve():
    n_str = None
    processed = 0
    root = DirNode()  # Віртуальний корінь на глибині -1

    for line in sys.stdin:
        cleaned = line.strip()
        if not cleaned:
            continue

        if n_str is None:
            n_str = int(cleaned)
            continue

        parts = cleaned.split("\\")
        root.insert_path(parts)
        processed += 1
        if processed == n_str:
            break

    if n_str is not None:
        root.print_tree(-1)


if __name__ == "__main__":
    solve()
