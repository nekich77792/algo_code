"""
Розв'язки завдань для самостійної роботи з курсу
«Алгоритми та структури даних» (Лабораторні роботи 1 та 2)

Теми:
- Лабораторна робота 1: Складність алгоритмів. Час виконання.
  Завдання: 1.3 a, b, d, e; 1.4 a, b, c
- Лабораторна робота 2: Складність алгоритмів. Асимптотична оцінка складності.
  Завдання: 2.10; 2.13 a, e, g; 2.14 a - i
"""

import math


# ==============================================================================
# ЛАБОРАТОРНА РОБОТА 1. Завдання 1.3
# ==============================================================================

def task_1_3_a(n: int) -> tuple[int, int]:
    """
    1.3 a)
    1 k += 1
    2 i = n
    3 while i > 0:
    4     i -= 1

    Час виконання:
    - Кількість ітерацій циклу: n (при n >= 0)
    - Рядок 1 (k += 1): 1 раз
    - Рядок 2 (i = n): 1 раз
    - Рядок 3 (while i > 0): n + 1 перевірок
    - Рядок 4 (i -= 1): n разів
    Точний час: T(n) = 2n + 3 (або c1*n + c0)
    Асимптотика: Theta(n) - лінійний час.
    """
    k = 0
    k += 1
    i = n
    iterations = 0
    while i > 0:
        iterations += 1
        i -= 1
    return k, iterations


def task_1_3_b(n: int) -> tuple[int, int]:
    """
    1.3 b)
    1 i = n
    2 while i > 1:
    3     k += 1
    4     i //= 2

    Час виконання:
    - Кількість ітерацій циклу: floor(log2(n)) (при n >= 1)
    - Рядок 1 (i = n): 1 раз
    - Рядок 2 (while i > 1): floor(log2(n)) + 1 перевірок
    - Рядок 3 (k += 1): floor(log2(n)) разів
    - Рядок 4 (i //= 2): floor(log2(n)) разів
    Точний час: T(n) = 3 * floor(log2(n)) + 2
    Асимптотика: Theta(log n) - логарифмічний час.
    """
    k = 0
    i = n
    iterations = 0
    while i > 1:
        iterations += 1
        k += 1
        i //= 2
    return k, iterations


def task_1_3_d(n: int) -> tuple[int, int]:
    """
    1.3 d)
    1 i = 0
    2 while i < n:
    3     j = 0
    4     while j < i * i:
    5         k += 1
    6         j += 1
    7     i += 1

    Час виконання:
    - Зовнішній цикл: n ітерацій (i = 0, 1, ..., n - 1)
    - Внутрішній цикл для кожного i: i^2 ітерацій
    - Загальна кількість ітерацій тіла (k += 1):
      sum_{i=0}^{n-1} i^2 = (n - 1) * n * (2n - 1) / 6
    - Точний час (усі операції):
      T(n) = n^3 - 1.5 * n^2 + 4.5 * n + 2
    Асимптотика: Theta(n^3) - кубічний час.
    """
    k = 0
    i = 0
    while i < n:
        j = 0
        while j < i * i:
            k += 1
            j += 1
        i += 1
    return k, (n - 1) * n * (2 * n - 1) // 6 if n > 0 else 0


def task_1_3_e(n: int) -> tuple[int, int]:
    """
    1.3 e)
    1 i = 1
    2 while i < n:
    3     j = 1
    4     while j < n:
    5         k += 1
    6         j *= 2
    7     i *= 2

    Час виконання:
    - Зовнішній цикл: p = ceil(log2(n)) ітерацій (для n >= 1)
    - Внутрішній цикл: q = ceil(log2(n)) ітерацій незалежно від i
    - Загальна кількість ітерацій тіла (k += 1):
      p * q = (ceil(log2(n)))^2
    - Точний час операцій:
      T(n) = 3 * (ceil(log2(n)))^2 + 4 * ceil(log2(n)) + 2
    Асимптотика: Theta(log^2 n) - квадратично-логарифмічний час.
    """
    k = 0
    i = 1
    while i < n:
        j = 1
        while j < n:
            k += 1
            j *= 2
        i *= 2
    expected = math.ceil(math.log2(n))**2 if n > 1 else 0
    return k, expected


# ==============================================================================
# ЛАБОРАТОРНА РОБОТА 1. Завдання 1.4
# ==============================================================================

def task_1_4_a_recursive(n: int, a: int) -> int:
    """Рекурентне визначення: T(n) = 1 при n <= a; T(n - a) + 1 при n > a."""
    if n <= a:
        return 1
    return task_1_4_a_recursive(n - a, a) + 1


def task_1_4_a_explicit(n: int, a: int) -> int:
    """Явний вигляд: T(n) = ceil(n / a)."""
    return math.ceil(n / a)


def task_1_4_b_recursive(n: int) -> int:
    """Рекурентне визначення: T(0) = 1; T(n) = T(n - 1) + 2^n при n >= 1."""
    if n == 0:
        return 1
    return task_1_4_b_recursive(n - 1) + (2 ** n)


def task_1_4_b_explicit(n: int) -> int:
    """Явний вигляд: T(n) = 2^(n + 1) - 1."""
    return 2 ** (n + 1) - 1


def task_1_4_c_recursive(n: int) -> int:
    """Рекурентне визначення: T(1) = 1; T(n) = 2*T([n / 2]) + 1 при n >= 2."""
    if n == 1:
        return 1
    return 2 * task_1_4_c_recursive(n // 2) + 1


def task_1_4_c_explicit(n: int) -> int:
    """
    Явний вигляд:
    Для довільного n >= 1: T(n) = 2^(floor(log2(n)) + 1) - 1.
    Зокрема, якщо n = 2^k: T(n) = 2n - 1.
    """
    return 2 ** (math.floor(math.log2(n)) + 1) - 1


# ==============================================================================
# ЛАБОРАТОРНА РОБОТА 2. Завдання 2.10
# ==============================================================================

def f_2_10(n: int) -> int:
    """
    Вихідна функція з умови:
    def f(n):
        sum = 0
        for i in range(1, n + 1):
            sum = sum + i
        return sum

    Складність: O(n) у найгіршому, найкращому та середньому випадках.
    Результат: Сума перших n натуральних чисел: sum = n * (n + 1) / 2.
    """
    total_sum = 0
    for i in range(1, n + 1):
        total_sum = total_sum + i
    return total_sum


def f_2_10_optimized(n: int) -> int:
    """
    Оптимізована функція:
    Використовує аналітичну формулу суми арифметичної прогресії.
    Складність: O(1) - сталий час виконання.
    Асимптотична оцінка покращена з O(n) до O(1).
    """
    return n * (n + 1) // 2


# ==============================================================================
# ЛАБОРАТОРНА РОБОТА 2. Завдання 2.13
# ==============================================================================
# a) T(0) = O(1), T(n) = T(n - 1) + O(1)   ==> T(n) = O(n)
# e) T(0) = O(1), T(n) = T(n - 1) + O(n)   ==> T(n) = O(n^2)
# g) T(1) = O(1), T(n) = a*T([n/a]) + O(1) ==> T(n) = O(n) (за Майстер-теоремою)


# ==============================================================================
# ЛАБОРАТОРНА РОБОТА 2. Завдання 2.14
# Алгоритми для обчислення виразів із заявленою асимптотичною оцінкою
# ==============================================================================

def compute_2_14_a(n: int) -> int:
    """
    2.14 a) sum_{i=0}^n i = O(n)
    Складність: n + 1 ітерацій по O(1) -> O(n).
    """
    total = 0
    for i in range(n + 1):
        total += i
    return total


def compute_2_14_b(n: int) -> int:
    """
    2.14 b) sum_{i=0}^n i^2 = O(n)
    Складність: n + 1 ітерацій по O(1) -> O(n).
    """
    total = 0
    for i in range(n + 1):
        total += i * i
    return total


def compute_2_14_c(n: int, a: float) -> float:
    """
    2.14 c) sum_{i=0}^n a^i = O(n)
    Ітеративне підтримання степеня cur_power = cur_power * a за O(1).
    Складність: n + 1 ітерацій по O(1) -> O(n).
    """
    total = 0.0
    cur_power = 1.0  # a^0
    for _ in range(n + 1):
        total += cur_power
        cur_power *= a
    return total


def compute_2_14_d(n: int) -> int:
    """
    2.14 d) sum_{i=0}^n i^i = O(n^2)  (0^0 = 1)
    Обчислення i^i за i множень: O(i).
    Загальний час: sum_{i=1}^n O(i) = O(n(n+1)/2) = O(n^2).
    """
    total = 1  # 0^0 = 1
    for i in range(1, n + 1):
        p = 1
        for _ in range(i):
            p *= i
        total += p
    return total


def compute_2_14_e(n: int) -> float:
    """
    2.14 e) prod_{i=1}^n 1 / (1 + i) = O(n)
    Складність: n ітерацій по O(1) -> O(n).
    """
    prod = 1.0
    for i in range(1, n + 1):
        prod *= 1.0 / (1.0 + i)
    return prod


def compute_2_14_f(n: int) -> float:
    """
    2.14 f) prod_{i=1}^n 1 / (1 + i!) = O(n)
    Ітеративне підтримання факторіала fact = fact * i за O(1).
    Складність: n ітерацій по O(1) -> O(n).
    """
    prod = 1.0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        prod *= 1.0 / (1.0 + fact)
    return prod


def compute_2_14_g(n: int, a: float) -> float:
    """
    2.14 g) prod_{i=1}^n a^i / (1 + i!) = O(n)
    Одночасне ітеративне підтримання p = p * a та fact = fact * i за O(1).
    Складність: n ітерацій по O(1) -> O(n).
    """
    prod = 1.0
    p = 1.0
    fact = 1
    for i in range(1, n + 1):
        p *= a
        fact *= i
        prod *= p / (1.0 + fact)
    return prod


def compute_2_14_h(n: int, m: int) -> float:
    """
    2.14 h) prod_{i=1}^n 1 / (1 + i^m) = O(n^m)
    Для фіксованого цілого m >= 1 піднесення до степеня займає m множень: O(m).
    Загальний час: n * O(m) = O(n) <= O(n^m).
    """
    prod = 1.0
    for i in range(1, n + 1):
        p = 1
        for _ in range(m):
            p *= i
        prod *= 1.0 / (1.0 + p)
    return prod


def compute_2_14_i(n: int) -> float:
    """
    2.14 i) prod_{i=1}^n 1 / (1 + i^i) = O(n^2)
    Обчислення i^i за i множень: O(i).
    Загальний час: sum_{i=1}^n O(i) = O(n^2).
    """
    prod = 1.0
    for i in range(1, n + 1):
        p = 1
        for _ in range(i):
            p *= i
        prod *= 1.0 / (1.0 + p)
    return prod


# ==============================================================================
# Перевірка та демонстрація
# ==============================================================================
if __name__ == "__main__":
    print("=== Демонстрація та самоперевірка розв'язків ===")

    # 1.3
    print("1.3 a) n=5 -> iters:", task_1_3_a(5)[1])
    print("1.3 b) n=16 -> iters:", task_1_3_b(16)[1])
    print("1.3 d) n=4 -> k:", task_1_3_d(4)[0], "formula:", task_1_3_d(4)[1])
    print("1.3 e) n=8 -> k:", task_1_3_e(8)[0], "formula:", task_1_3_e(8)[1])

    # 1.4
    print("1.4 a) n=10, a=3 -> rec:", task_1_4_a_recursive(10, 3), "exp:", task_1_4_a_explicit(10, 3))
    print("1.4 b) n=4 -> rec:", task_1_4_b_recursive(4), "exp:", task_1_4_b_explicit(4))
    print("1.4 c) n=10 -> rec:", task_1_4_c_recursive(10), "exp:", task_1_4_c_explicit(10))

    # 2.10
    print("2.10 n=10 -> f:", f_2_10(10), "optimized:", f_2_10_optimized(10))

    # 2.14
    print("2.14 a) n=5 ->", compute_2_14_a(5))
    print("2.14 b) n=5 ->", compute_2_14_b(5))
    print("2.14 c) n=5, a=2 ->", compute_2_14_c(5, 2))
    print("2.14 d) n=4 ->", compute_2_14_d(4))
    print("2.14 e) n=5 ->", compute_2_14_e(5))
    print("2.14 f) n=5 ->", compute_2_14_f(5))
    print("2.14 g) n=5, a=2 ->", compute_2_14_g(5, 2))
    print("2.14 h) n=5, m=3 ->", compute_2_14_h(5, 3))
    print("2.14 i) n=4 ->", compute_2_14_i(4))
    print("Усі розв'язки успішно виконані!")
