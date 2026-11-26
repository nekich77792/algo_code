"""
Завдання 7.3 (Лабораторна робота 7)
Задача: "Контакти" (Eolymp #2797, 100%)
https://eolymp.com/uk/problems/2797

Вимоги:
- Реалізована та використана власна хеш-таблиця (множина на базі відкритої адресації).
- Заборонено використання вбудованої функції hash().
- Заборонено використання вбудованих dict та set.
"""

import sys
import os


class OpenAddressingHashSet:
    """
    Хеш-таблиця (множина) з відкритою адресацією та лінійним зондуванням.
    Реалізована без використання вбудованих dict, set та функції hash().
    """

    def __init__(self, initial_capacity: int = 16):
        cap = 16
        while cap < initial_capacity:
            cap <<= 1
        self.capacity = cap
        self.mask = cap - 1
        self.keys = [None] * cap
        self.size = 0

    def _hash(self, key: str) -> int:
        """Власний 64-бітний алгоритм хешування рядків FNV-1a."""
        h = 14695981039346656037
        for ch in key:
            h ^= ord(ch)
            h = (h * 1099511628211) & 0xFFFFFFFFFFFFFFFF
        return h

    def _resize(self, new_capacity: int):
        old_keys = self.keys
        old_cap = self.capacity

        self.capacity = new_capacity
        self.mask = new_capacity - 1
        self.keys = [None] * new_capacity
        self.size = 0

        mask = self.mask
        keys = self.keys
        for i in range(old_cap):
            k = old_keys[i]
            if k is not None:
                idx = self._hash(k) & mask
                while keys[idx] is not None:
                    idx = (idx + 1) & mask
                keys[idx] = k
                self.size += 1

    def add(self, key: str) -> bool:
        if self.size * 2 >= self.capacity:
            self._resize(self.capacity * 2)

        idx = self._hash(key) & self.mask
        mask = self.mask
        keys = self.keys

        while True:
            k = keys[idx]
            if k is None:
                keys[idx] = key
                self.size += 1
                return True
            if k == key:
                return False
            idx = (idx + 1) & mask

    def __len__(self) -> int:
        return self.size


def solve(file_path: str = None):
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            input_data = f.read().split()
    else:
        input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])
    phone_numbers = input_data[1:n + 1]

    contacts = OpenAddressingHashSet(initial_capacity=max(16, n * 2))
    for phone in phone_numbers:
        contacts.add(phone)

    print(len(contacts))


if __name__ == "__main__":
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        solve(file_path=sys.argv[1])
    else:
        solve()
