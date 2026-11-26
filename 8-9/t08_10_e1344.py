"""
Лабораторна робота 8. Завдання 8.10
Задача: "Особові справи" (Eolymp #1344, 100%)
https://eolymp.com/uk/problems/1344

Алгоритм: Сортування вставкою (Insertion Sort)
Критерій: Сортування спочатку за номером класу (1..11), потім за буквою класу, потім за прізвищем.
Вимога: Без використання регулярних виразів (модуля re).
"""

import sys


def parse_class(class_str: str) -> tuple:
    """
    Виділяє числову частину класу та літеру без використання регулярних виразів.
    Наприклад: '9A' -> (9, 'A'), '10B' -> (10, 'B'), '11' -> (11, '').
    """
    num_part = ""
    letter_part = ""
    for ch in class_str.strip():
        if ch.isdigit():
            num_part += ch
        else:
            letter_part += ch
    class_num = int(num_part) if num_part else 0
    return (class_num, letter_part)


def is_less(s1: dict, s2: dict) -> bool:
    """
    Порівняння двох учнів:
    1. Номер класу (число: 9 < 10)
    2. Буква класу (літера: 'A' < 'B')
    3. Прізвище та ім'я
    """
    k1 = (s1["class_num"], s1["class_letter"], s1["name"])
    k2 = (s2["class_num"], s2["class_letter"], s2["name"])
    return k1 < k2


def insertion_sort_students(students: list):
    """Класичне сортування вставкою списку учнів."""
    n = len(students)
    for i in range(1, n):
        key_item = students[i]
        j = i - 1
        while j >= 0 and is_less(key_item, students[j]):
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key_item


def solve():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return

    n = int(lines[0])
    students = []
    idx = 1
    for _ in range(n):
        if idx + 2 < len(lines):
            name = lines[idx]
            s_class = lines[idx + 1]
            b_date = lines[idx + 2]
            class_num, class_letter = parse_class(s_class)
            students.append({
                "name": name,
                "class": s_class,
                "bdate": b_date,
                "class_num": class_num,
                "class_letter": class_letter
            })
            idx += 3

    insertion_sort_students(students)

    # Вивід: для кожного учня 3 рядки (ПІБ, клас, дата народження)
    for s in students:
        print(s["name"])
        print(s["class"])
        print(s["bdate"])


if __name__ == "__main__":
    solve()
