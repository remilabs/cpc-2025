from math import log2 as log
h,w=map(int,input().split())
x,y=map(int,input().split())
a,b=max(h,w),min(h,w)
c,d=max(x,y),min(x,y)
print((int(log(a))-int(log(c))) + (int(log(b))-int(log(d))))