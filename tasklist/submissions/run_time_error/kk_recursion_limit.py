import functools


n, m = map(int, input().split())

task_times = {i: int(input()) for i in range(n)}
task_graph = {i: [] for i in range(n)}
is_sink = {i: True for i in range(n)}

for _ in range(m):
    ai, bi = map(int, input().split())
    task_graph[bi].append(ai)
    is_sink[ai] = False


cache = {}


def dfs(v, total):
    if len(task_graph[v]) == 0:
        return task_times[v]
    path_totals = []
    for c in task_graph[v]:
        if (c, total) not in cache:
            pt = dfs(c, total)
            cache[(c, total)] = pt
        path_totals.append(cache[(c, total)] + task_times[v])
    return max(path_totals)


totals = []
for i in range(n):
    if is_sink[i]:
        totals.append(dfs(i, 0))

print(max(totals))
