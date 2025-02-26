from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(200000)

r = lambda: [*map(int,input().split())]
n,m = r()
times = [int(input()) for _ in range(n)]
deps = [r() for _ in range(m)]
g = [[] for _ in range(n)]
for a,b in deps:
  g[b].append(a)

@lru_cache(None)
def dfs(a):
  m = 0
  for b in g[a]:
    m = max(m, dfs(b))
  return m + times[a]

m = 0
for i in range(n):
  m =max(m, dfs(i))
print(m)
