from functools import lru_cache
from bisect import bisect_right as bisect
def rot(x,y,k):
  if k%4 == 0:
    return x,y
  return rot(y,-x, k-1)

mod = 10**9+7

@lru_cache(None)
def dp(x,y):
  # Should never happen
  if x == 0 and y == 0:
    assert False

  # If on an axis, only one way to get to destination
  if x == 0 or y == 0:
    return 1

  # How many times to rotate
  k = 0
  if x < 0:
    k = 1 if y > 0 else 2
  elif y < 0:
    k = 3
  total = 0
  x,y = rot(x,y,k)
  #bisect to find the highest point that is less than/equal to y
  myi = bisect(key_points[k][x], y) - 1
  my = -y
  if myi >= 0:
    my = max(key_points[k][x][myi], my)

  for i in range(0, my, -1):
    total += dp(*rot(x,i,4-k))
  return total % mod


r = lambda:[*map(int,input().split())]

x,y,n=r()
points = [r() for _ in range(n)]
rotated = [[rot(a,b,k) for a,b in points] for k in range(4)]
key_points = [[[] for i in range(501)] for _ in range(4)]
for i in range(4):
  for a, b in rotated[i]:
    if a <= 0: continue
    key_points[i][a].append(b)
for i in range(4):
  for j in range(501):
    key_points[i][j].sort()

print(dp(x,y))
