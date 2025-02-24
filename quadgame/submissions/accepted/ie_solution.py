from collections import Counter
n=int(input())
a,b,*c=list(map(int,input().split()))
c=Counter(c)
mn=float('inf')
for a,b in [(a,b),(b,a)]:
    for r in c:
        c[r]-=1
        l=(abs(a-r)**2+b**2)**.5
        if l in c and c[l]:
            mn=min(mn,a+b+r+l)
        c[r]+=1
print(int(mn) if mn!=float('inf') else -1)