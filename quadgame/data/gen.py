N = 10**5
from collections import Counter
from math import inf
from random import randint


def solve(a, b, rods):
    c = Counter([rod**2 for rod in rods])

    answer = inf

    def attach(i, a, b):
        difference = abs(i - a)
        target = difference**2 + b**2
        if c[target] > 0:
            return a + b + int(target ** (1 / 2)) + i
        return inf

    for i in rods:
        c[i**2] -= 1
        answer = min(answer, attach(i, a, b))
        answer = min(answer, attach(i, b, a))
        c[i**2] += 1

    return answer if answer != inf else -1


with open("large.in", "w") as f, open("large.out", "w") as o:
    print("generating testcase")
    print(N, file=f)
    rods = [randint(1, N) for _ in range(N)]
    print("rod counts", len(rods))
    print(" ".join(map(str, rods)), file=f)
    a, b, *r = rods
    print("trying to solve")
    p = solve(a, b, r)
    print(p)
    print(p, file=o)
