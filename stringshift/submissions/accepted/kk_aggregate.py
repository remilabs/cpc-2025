s = input()
n = int(input())

shift = 0

for _ in range(n):
    d, x = input().split()
    shift += (-1 if d == "r" else 1) * int(x)

for i in range(len(s)):
    c = s[(i + shift) % len(s)]
    print(c, end="")
print()
