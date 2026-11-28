"""
Лабораторна робота 22. Завдання 22.4
Задача: "Маршрути в горах" (Eolymp #122, 100%)
https://eolymp.com/uk/problems/122

Алгоритм: Пошук простих шляхів довжиною не більше d за допомогою зворотного BFS та DFS з відсіканням.
"""

import sys

sys.setrecursionlimit(50000)


def compute_distances_to_target(n: int, target: int, rev_adj: list, limit: int) -> list:
    """Знаходить найкоротшу відстань від кожної вершини до target за допомогою BFS."""
    unreachable = limit + 1
    dist = [unreachable] * (n + 1)
    dist[target] = 0

    queue = [target]
    head = 0

    while head < len(queue):
        u = queue[head]
        head += 1
        d_next = dist[u] + 1
        if d_next > limit:
            continue
        for prev_v in rev_adj[u]:
            if dist[prev_v] == unreachable:
                dist[prev_v] = d_next
                queue.append(prev_v)

    return dist


def count_simple_routes(n: int, a: int, b: int, d: int, adj: list, adj_sets: list, rev_adj: list) -> int:
    """Підраховує кількість простих шляхів з a до b довжиною не більше d."""
    if a == b:
        return 1

    dist_to_b = compute_distances_to_target(n, b, rev_adj, d)
    if dist_to_b[a] > d:
        return 0

    visited = [False] * (n + 1)
    visited[a] = True

    def dfs(u: int, rem_days: int) -> int:
        if rem_days == 1:
            return 1 if b in adj_sets[u] else 0

        total = 0
        next_rem = rem_days - 1
        for v in adj[u]:
            if v == b:
                total += 1
            elif not visited[v] and dist_to_b[v] <= next_rem:
                visited[v] = True
                total += dfs(v, next_rem)
                visited[v] = False
        return total

    return dfs(a, d)


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    it = iter(tokens)
    n = int(next(it))
    k = int(next(it))
    a = int(next(it))
    b = int(next(it))
    d = int(next(it))

    adj_sets = [set() for _ in range(n + 1)]
    adj = [[] for _ in range(n + 1)]
    rev_adj = [[] for _ in range(n + 1)]

    for _ in range(k):
        u = int(next(it))
        v = int(next(it))
        if u != v and v not in adj_sets[u]:
            adj_sets[u].add(v)
            adj[u].append(v)
            rev_adj[v].append(u)

    result = count_simple_routes(n, a, b, d, adj, adj_sets, rev_adj)
    sys.stdout.write(str(result) + "\n")


if __name__ == "__main__":
    solve()
