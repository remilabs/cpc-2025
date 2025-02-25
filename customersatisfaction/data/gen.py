from random import randint
n=randint(1,20)
m=randint(1,150)
print(n,m)
for _ in range(n):
    print(randint(0,m))
c=randint(0,n*m)
print(c)
for _ in range(c):
    print(randint(0,n-1),randint(0,m-1))
h=randint(0,n*m)
print(h)
for _ in range(h):
    print(randint(0,m-1),randint(0,n-1))
