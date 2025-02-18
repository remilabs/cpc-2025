from math import inf

n=int(input())
a,b,*rods = [*map(int,input().split())]

answer = inf

def attach(i,a,b):
  difference = abs(rods[i] - a)
  options = [inf]
  for j in range(len(rods)):
    if i == j: continue
    if rods[j]**2 == difference**2 + b**2:
      options.append(a+b+rods[i]+rods[j])
  return min(options)

for i in range(len(rods)):
  answer = min(answer, attach(i,a,b))
  answer = min(answer, attach(i,b,a))

print(answer if answer != inf else -1)
