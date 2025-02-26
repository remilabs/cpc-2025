from random import randint

n = 100000
m = 500000

print(n,m)
for i in range(n):
  print(randint(1,10000))

total = 0
deps = [set() for _ in range(n)]
for i in range(1, n):
  for _ in range(10):
    deps[i].add(randint(0,i-1))
  total += len(deps[i])

if total < m:
  assert 0
while total > m:
  i = randint(1, n-1)
  if len(deps[i]) > 0:
    deps[i].pop()
    total -= 1


if total != m:
  assert 0

for i in range(n-1, -1, -1):
  if len(deps[i]):
    for j in deps[i]:
      print(j, i)
