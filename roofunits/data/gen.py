import random

with open("secret/3.in", "w") as f:
    n = 100_000
    print(n, file=f)
    for _ in range(n):
        if random.random() < 0.5:
            x = random.randint(0, 1_000)
            print(f"{x}/12", file=f)
        else:
            x = random.randint(0, 899)
            print(f"{x/10:.1f}", file=f)
