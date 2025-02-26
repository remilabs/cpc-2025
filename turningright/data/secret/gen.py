from random import randint
n = 1000
m = 100
print(m,m,n)
b = set()
r = lambda: randint(1,m-1) * [-1, 1][randint(0,1)]
while len(b) < n:
  b.add((r(),r()))
for t in b:
  print(*t)
