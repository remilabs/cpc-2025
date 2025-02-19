from math import ceil,log2 as log
h,w=map(int,input().split())
x,y=map(int,input().split())
a,b=max(h,w),min(h,w)
c,d=max(x,y),min(x,y)
t=0
while a>c:
    if a>=c*2:
        a=(a+1)//2
        t+=1
    else:
        a=c
        t+=1
while b>d:
    if b>=d*2:
        b=(b+1)//2
        t+=1
    else:
        b=d
        t+=1
print(t)
