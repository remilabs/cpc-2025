from collections import Counter
from math import inf

n=int(input())
a,b,*rods = [*map(int,input().split())]

c = Counter([rod**2 for rod in rods])

answer = inf

def attach(i,a,b):
  difference = abs(i - a)
  target = difference**2 + b**2
  if c[target] > 0:
    return a + b + int(target**(1/2)) + i
  return inf
  
for i in rods:
  c[i**2] -= 1
  answer = min(answer, attach(i,a,b))
  answer = min(answer, attach(i,b,a))
  c[i**2] += 1

print(answer if answer != inf else -1)
