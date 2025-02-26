from random import randint
n = 10000
print(500,500,10000)
b = set()
r = lambda: randint(1,499) * [-1, 1][randint(0,1)]
while len(b) < n:
  b.add((r(),r()))
for t in b:
  print(*t)
