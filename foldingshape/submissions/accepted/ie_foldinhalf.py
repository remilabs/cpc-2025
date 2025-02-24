from math import ceil,log2 as log
a,b=map(int,input().split())
c,d=map(int,input().split())
oa,ob=a,b
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
a,b=oa,ob
c,d=d,c
t2 = 0
while a>c:
    if a>=c*2:
        a=(a+1)//2
        t2+=1
    else:
        a=c
        t2+=1
while b>d:
    if b>=d*2:
        b=(b+1)//2
        t2+=1
    else:
        b=d
        t2+=1
print(min(t,t2))

