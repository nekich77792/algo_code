"""
Реалізація каталогу бібліотеки художніх книг за допомогою хеш-таблиці з відкритою адресацією.
Вимоги:
- Без використання вбудованої функції hash()
- Без використання dict та set
- Відкрита адресація з лінійним зондуванням та очищенням видалених елементів
"""


class OpenAddressingMap:
    _DELETED = object()

    def __init__(self, initial_capacity=64):
        self.capacity = initial_capacity
        self.size = 0
        self.deleted_count = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def _hash(self, key: str) -> int:
        # 64-бітний алгоритм хешування FNV-1a (без використання вбудованого hash())
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
        self.keys = [None] * new_capacity
        self.values = [None] * new_capacity
        self.size = 0
        self.deleted_count = 0

        for i in range(old_cap):
            k = old_keys[i]
            if k is not None and k is not self._DELETED:
                self.put(k, old_values[i])

    def put(self, key: str, value) -> bool:
        # Фактор завантаження: якщо зайнято більше 50% слотів (включаючи tombstone)
        if (self.size + self.deleted_count) * 2 >= self.capacity:
            if self.size * 4 < self.capacity:
                new_cap = self.capacity  # очищення tombstones без подвоєння
            else:
                new_cap = self.capacity * 2
            self._resize(new_cap)

        idx = self._hash(key) % self.capacity
        first_deleted = -1

        while True:
            k = self.keys[idx]
            if k is None:
                if first_deleted != -1:
                    idx = first_deleted
                    self.deleted_count -= 1
                self.keys[idx] = key
                self.values[idx] = value
                self.size += 1
                return True
            elif k is self._DELETED:
                if first_deleted == -1:
                    first_deleted = idx
            elif k == key:
                self.values[idx] = value
                return False
            idx = (idx + 1) % self.capacity

    def get(self, key: str):
        idx = self._hash(key) % self.capacity
        while True:
            k = self.keys[idx]
            if k is None:
                return None
            elif k is not self._DELETED and k == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity

    def contains(self, key: str) -> bool:
        return self.get(key) is not None

    def delete(self, key: str) -> bool:
        idx = self._hash(key) % self.capacity
        while True:
            k = self.keys[idx]
            if k is None:
                return False
            elif k is not self._DELETED and k == key:
                self.keys[idx] = self._DELETED
                self.values[idx] = None
                self.size -= 1
                self.deleted_count += 1
                return True
            idx = (idx + 1) % self.capacity


# Глобальні змінні каталогу
_books = None
_authors = None


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global _books, _authors
    _books = OpenAddressingMap(initial_capacity=8192)
    _authors = OpenAddressingMap(initial_capacity=2048)


def addBook(author: str, title: str):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    key = author + "\x00" + title
    if not _books.contains(key):
        _books.put(key, True)
        titles = _authors.get(author)
        if titles is None:
            _authors.put(author, [title])
        else:
            titles.append(title)


def find(author: str, title: str) -> bool:
    """ Перевіряє чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    key = author + "\x00" + title
    return _books.contains(key)


def delete(author: str, title: str):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    key = author + "\x00" + title
    if _books.delete(key):
        titles = _authors.get(author)
        if titles is not None:
            try:
                titles.remove(title)
            except ValueError:
                pass


def findByAuthor(author: str) -> list:
    """ Повертає список книг заданого автора.
    Якщо бібліотека не містить книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    titles = _authors.get(author)
    if not titles:
        return []
    return sorted(titles)
