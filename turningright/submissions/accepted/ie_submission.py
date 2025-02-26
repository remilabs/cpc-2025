from functools import lru_cache
from collections import defaultdict

def rotateccw(p,t):
    if not t:
        return p
    return rotateccw((-p[1],p[0]),t-1)

@lru_cache(None)
def solve(x,y):
    if y==0 or x==0: return 1
    q=0
    if x>0:q=1 if y>0 else 2
    elif y<0:q=3
    x,y=rotateccw((x,y),q)
    c=0
    for i in range(0,-x):
        for a in obs[q][y]:
            if x<=a<=i: break
        else: c += solve(*rotateccw((i,y),4-q))
    return c % MOD

MOD=10**9+7
x,y,n=map(int,input().split())
ob=set(tuple(map(int,input().split())) for _ in range(n))
obs={}
obs={i:defaultdict(set) for i in range(4)}
for i in range(4):
    for o in ob:
        a,b=rotateccw(o,i)
        obs[i][b].add(a)
print(solve(x,y))
