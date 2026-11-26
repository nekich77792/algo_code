"""
Завдання 7.4 (Лабораторна робота 7)
Задача: "Перевірка орфографії" (Eolymp #2195, 100%)
https://eolymp.com/uk/problems/2195

Вимоги:
- Реалізована та використана власна хеш-таблиця з відкритою адресацією.
- Заборонено використання вбудованої функції hash().
- Заборонено використання вбудованих dict та set.
"""

import sys
import os
import re


class OpenAddressingHashMap:
    """
    Хеш-таблиця (асоціативний масив) з відкритою адресацією та лінійним зондуванням.
    Реалізована без використання вбудованих dict, set та функції hash().
    """

    def __init__(self, initial_capacity: int = 16):
        cap = 16
        while cap < initial_capacity:
            cap <<= 1
        self.capacity = cap
        self.mask = cap - 1
        self.keys = [None] * cap
        self.values = [None] * cap
        self.size = 0

    def _hash(self, key: str) -> int:
        """Власний 64-бітний хеш FNV-1a."""
        h = 14695981039346656037
        for ch in key:
            h ^= ord(ch)
            h = (h * 1099511628211) & 0xFFFFFFFFFFFFFFFF
        return h

    def _resize(self, new_capacity: int):
        old_keys = self.keys
        old_values = self.values
        old_cap = self.capacity

        self.capacity = new_capacity
        self.mask = new_capacity - 1
        self.keys = [None] * new_capacity
        self.values = [None] * new_capacity
        self.size = 0

        mask = self.mask
        keys = self.keys
        values = self.values

        for i in range(old_cap):
            k = old_keys[i]
            if k is not None:
                idx = self._hash(k) & mask
                while keys[idx] is not None:
                    idx = (idx + 1) & mask
                keys[idx] = k
                values[idx] = old_values[i]
                self.size += 1

    def put(self, key: str, value) -> bool:
        if self.size * 2 >= self.capacity:
            self._resize(self.capacity * 2)

        idx = self._hash(key) & self.mask
        mask = self.mask
        keys = self.keys
        values = self.values

        while True:
            k = keys[idx]
            if k is None:
                keys[idx] = key
                values[idx] = value
                self.size += 1
                return True
            if k == key:
                values[idx] = value
                return False
            idx = (idx + 1) & mask

    def get(self, key: str):
        idx = self._hash(key) & self.mask
        mask = self.mask
        keys = self.keys

        while True:
            k = keys[idx]
            if k is None:
                return None
            if k == key:
                return self.values[idx]
            idx = (idx + 1) & mask

    def contains(self, key: str) -> bool:
        return self.get(key) is not None

    def __len__(self) -> int:
        return self.size


def check_spelling(vocab_words: list, text_content: str) -> str:
    vocab = OpenAddressingHashMap(initial_capacity=max(16, len(vocab_words) * 2))

    for word in vocab_words:
        w = word.strip().lower()
        if w:
            vocab.put(w, False)

    words_in_text = re.findall(r'[a-zA-Z]+', text_content)
    used_vocab_count = 0

    for raw_word in words_in_text:
        w = raw_word.lower()
        status = vocab.get(w)
        if status is None:
            return "Some words from the text are unknown."
        elif status is False:
            vocab.put(w, True)
            used_vocab_count += 1

    if used_vocab_count == len(vocab):
        return "Everything is going to be OK."
    else:
        return "The usage of the vocabulary is not perfect."


def solve(file_path: str = None):
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            raw_input = f.read().splitlines()
    else:
        raw_input = sys.stdin.read().splitlines()

    if not raw_input:
        return

    first_line = raw_input[0].split()
    n = int(first_line[0])
    m = int(first_line[1])

    vocab_words = raw_input[1:1 + n]
    text_lines = raw_input[1 + n:1 + n + m]
    text_content = "\n".join(text_lines)

    result = check_spelling(vocab_words, text_content)
    print(result)


if __name__ == "__main__":
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        solve(file_path=sys.argv[1])
    else:
        solve()
