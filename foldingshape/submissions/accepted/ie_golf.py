from math import ceil,log2 as log
a,b=map(int,input().split())
c,d=map(int,input().split())
print(min(sum(ceil(log(x)-log(y))if x>y else 0 for x,y in p)for p in[[(a,c),(b,d)],[(a,d),(b,c)]]))