"""
Лабораторна робота 19. Завдання 19.4
Задача: "Черга з пріоритетами" (Eolymp #4847, 100%)
https://eolymp.com/uk/problems/4847

Вказівка: Описати пріоритетну чергу на базі двійкової купи.
"""

import sys


class PriorityQueue:
    """
    Пріоритетна черга на базі максимальної двійкової купи з підтримкою
    операцій ADD, POP та CHANGE зі складністю O(log n) за рахунок індексної мапи.
    """

    def __init__(self):
        self._heap_priorities = []
        self._heap_ids = []
        # Відображення item_id -> індекс у купі для пошуку та модифікації за O(1)
        self._id_to_idx = {}

    def _swap(self, i: int, j: int) -> None:
        """Міняє місцями два елементи в купі та оновлює мапу індексів."""
        priorities = self._heap_priorities
        ids = self._heap_ids
        pos = self._id_to_idx

        id_i = ids[i]
        id_j = ids[j]

        priorities[i], priorities[j] = priorities[j], priorities[i]
        ids[i], ids[j] = id_j, id_i

        pos[id_i] = j
        pos[id_j] = i

    def _sift_up(self, idx: int) -> None:
        """Просіювання елемента вгору для відновлення властивості купи."""
        priorities = self._heap_priorities
        while idx > 0:
            parent = (idx - 1) >> 1
            if priorities[idx] <= priorities[parent]:
                break
            self._swap(idx, parent)
            idx = parent

    def _sift_down(self, idx: int) -> None:
        """Просіювання елемента вниз для відновлення властивості купи."""
        priorities = self._heap_priorities
        size = len(priorities)
        half = size >> 1

        while idx < half:
            left = (idx << 1) + 1
            right = left + 1
            best = left

            if right < size and priorities[right] > priorities[left]:
                best = right

            if priorities[idx] >= priorities[best]:
                break

            self._swap(idx, best)
            idx = best

    def add(self, item_id: str, priority: int) -> None:
        """Додає новий елемент у чергу з пріоритетом."""
        idx = len(self._heap_ids)
        self._heap_ids.append(item_id)
        self._heap_priorities.append(priority)
        self._id_to_idx[item_id] = idx
        self._sift_up(idx)

    def pop(self) -> tuple:
        """Вилучає та повертає елемент з найбільшим пріоритетом."""
        top_id = self._heap_ids[0]
        top_priority = self._heap_priorities[0]

        last_idx = len(self._heap_ids) - 1
        if last_idx > 0:
            self._swap(0, last_idx)

        self._heap_ids.pop()
        self._heap_priorities.pop()
        del self._id_to_idx[top_id]

        if self._heap_ids:
            self._sift_down(0)

        return top_id, top_priority

    def change(self, item_id: str, new_priority: int) -> None:
        """Змінює пріоритет елемента item_id на new_priority."""
        idx = self._id_to_idx[item_id]
        old_priority = self._heap_priorities[idx]
        self._heap_priorities[idx] = new_priority

        if new_priority > old_priority:
            self._sift_up(idx)
        elif new_priority < old_priority:
            self._sift_down(idx)


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    pq = PriorityQueue()
    output = []
    i = 0
    total = len(tokens)

    while i < total:
        cmd = tokens[i]
        if cmd == "ADD":
            item_id = tokens[i + 1]
            priority = int(tokens[i + 2])
            pq.add(item_id, priority)
            i += 3
        elif cmd == "POP":
            top_id, top_priority = pq.pop()
            output.append(f"{top_id} {top_priority}")
            i += 1
        elif cmd == "CHANGE":
            item_id = tokens[i + 1]
            new_priority = int(tokens[i + 2])
            pq.change(item_id, new_priority)
            i += 3
        else:
            i += 1

    if output:
        sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    solve()
