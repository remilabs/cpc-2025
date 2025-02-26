from random import randint, shuffle
n=100000
print(n)
o = [115, 50000]
l = [277, 50000 + 252]
while len(l) < n - 2:
  l.append(randint(1, n))
shuffle(l)
print(*o, *l)

