import math
r=lambda:map(int,input().split())
a,b=r()
c,d=r()
print(min(sum(math.ceil(math.log2(x)-math.log2(y))if x>y else 0 for x,y in p)for p in[[(a,c),(b,d)],[(a,d),(b,c)]]))