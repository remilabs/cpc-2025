x = y = 200
n = 10000
print(x, y, n)

total = 0
for i in range(-x, 0):
  if total == n: break
  for j in range(y, 0, -1):
    print(i,j)
    total += 1
    if total == n: break
  
  

