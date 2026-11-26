"""
Завдання 6.3 (Лабораторна робота 6)
Задача: "Бібліотека художніх книг" (Каталог бібліотеки на хеш-таблиці з відкритою адресацією)
Репозиторій: https://github.com/krenevych/algo/tree/master/labs/L06/task3

Вимоги:
- Реалізована та використана власна хеш-таблиця з відкритою адресацією.
- Заборонено використання вбудованої функції hash().
- Заборонено використання вбудованих dict та set.
- Файл реалізації інтерфейсу каталогу: task6_3/user.py
- Тестова програма: task6_3/main.py
"""

import os
import sys
import subprocess

# Імпортуємо модуль user з папки task6_3
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'task6_3'))
import user
from user import OpenAddressingMap, init, addBook, find, delete, findByAuthor


def run_benchmark():
    """
    Запускає офіційний тестовий скрипт main.py з папки task6_3,
    який проводить 100 000 випадкових операцій та вимірює час виконання.
    """
    task_dir = os.path.join(os.path.dirname(__file__), 'task6_3')
    print("Запуск перевірки task6_3/main.py (100 000 операцій)...")
    result = subprocess.run([sys.executable, 'main.py'], cwd=task_dir, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Помилки:", result.stderr)
    return result.returncode == 0


if __name__ == "__main__":
    run_benchmark()
