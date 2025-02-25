from collections import defaultdict
from functools import lru_cache
n,m=map(int,input().split())
ts=[]
for _ in range(n):
    ts.append(int(input()))
adj=defaultdict(set)
for _ in range(m):
    a,b=map(int,input().split())
    adj[b].add(a)

@lru_cache(None)
def dfs(node):
    if node not in adj:
        return ts[node]
    t=0
    for neigh in adj[node]:
        t=max(t,dfs(neigh))
    return ts[node]+t
t=0
for i in range(n):
    t=max(t,dfs(i))
print(t)
