import random


N = 10**6
S = 10**5

with open("large.in", "w") as f:
    s = "".join(chr(i % 26 + 65) for i in range(S))
    print(s, file=f)
    print(N, file=f)
    for _ in range(N):
        op = "l" if random.random() < 0.5 else "r"
        v = random.randint(0, N)
        print(op, v, file=f)
