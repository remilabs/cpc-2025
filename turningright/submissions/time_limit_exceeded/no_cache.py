def rot(x,y,k):
  if k == 0:
    return x,y
  return rot(y,-x, k-1)

mod = 10**9+7

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

  # rotate everything to be in quadrant 1
  x,y = rot(x,y,k)
  rotated = [rot(a,b,k) for a,b in points]

  total = 0
  for i in range(0, -y, -1):
    for a,b in rotated:

      # Can we travel from x,y to x,i?
      if a == x and y >= b >= i:
        break
    else:
      total += dp(*rot(x,i,4-k))
  return total % mod


def read():
  return list(map(int,input().split()))

x,y,n=read()
points = [read() for _ in range(n)]

print(dp(x,y))
