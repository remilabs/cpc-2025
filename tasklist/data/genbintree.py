# bin tree with last task as root
# n=100000
# m=n-1
# print(n,m)
# for _ in range(n):
#     print(1)
# for i in range(1,m+1):
#     if i==0:
#         continue
#     print(i,(i-1)//2)

# bin tree with first task as root
n=100000
m=n-1
print(n,m)
for _ in range(n):
    print(1)
for i in range(1,m+1):
    if i==0:
        continue
    print((i-1)//2,i)