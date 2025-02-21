import math
from collections import Counter

n = int(input())
rods = list(map(int, input().split()))

a, b, *rem = rods

rem_set = set(rem)
rem_counts = Counter(rem)


def get_hyp(rod, a, b):
    leg = max(b, rod)
    opp = min(b, rod)
    return math.sqrt(a**2 + (leg - opp) ** 2)


best = math.inf
best_rods = ()
for rod in rem_set:
    hyp_a = get_hyp(rod, a, b)
    if hyp_a in rem_set and rem_counts[hyp_a] > (1 if hyp_a == rod else 0):
        best = min(best, hyp_a + rod)
        best_rods = (rod, hyp_a)

if best == math.inf:
    print(-1)
else:
    print(int(best + a + b))
