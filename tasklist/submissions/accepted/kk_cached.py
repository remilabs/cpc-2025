# import functools
import sys

sys.setrecursionlimit(10**5)

n, m = map(int, input().split())

task_times = [int(input()) for _ in range(n)]
task_graph = [[] for _ in range(n)]
for _ in range(m):
    ai, bi = map(int, input().split())
    task_graph[bi].append(ai)

cache = [-1] * n

def dfs(v):
    if cache[v] != -1:
        return cache[v]
    m = 0
    for c in task_graph[v]:
        m = max(m, dfs(c))
    cache[v] = m + task_times[v]
    return cache[v]


m = 0
for i in range(n):
    m = max(m, dfs(i))

print(m)
