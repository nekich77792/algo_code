"""
Лабораторна робота 22. Завдання 22.5
Задача: "Підпал" (Eolymp #4369, 100%)
https://eolymp.com/uk/problems/4369

Алгоритм: Мультиджерельний BFS для моделювання поширення вогню графом.
"""

import sys


def find_last_burning_vertex(n: int, adj: list, sources: list) -> tuple:
    """
    Знаходить час займання останньої вершини та її найменший номер
    за допомогою мультиджерельного пошуку в ширину (BFS).
    """
    burn_time = [-1] * (n + 1)
    queue = []
    head = 0

    # Усі початкові точки підпалу починають горіти одночасно у момент 0
    for s in sources:
        if burn_time[s] == -1:
            burn_time[s] = 0
            queue.append(s)

    while head < len(queue):
        u = queue[head]
        head += 1
        t_next = burn_time[u] + 1
        for v in adj[u]:
            if burn_time[v] == -1:
                burn_time[v] = t_next
                queue.append(v)

    max_time = -1
    best_v = 1
    for v in range(1, n + 1):
        if burn_time[v] > max_time:
            max_time = burn_time[v]
            best_v = v

    return max_time, best_v


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    k = int(next(it))
    sources = [int(next(it)) for _ in range(k)]

    max_time, last_vertex = find_last_burning_vertex(n, adj, sources)
    sys.stdout.write(f"{max_time}\n{last_vertex}\n")


if __name__ == "__main__":
    solve()
