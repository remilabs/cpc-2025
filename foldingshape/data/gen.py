import random
import math

N = 10_000_000

K = 10


def solve_1(h, w, hh, ww):
    h, w = max(h, w), min(h, w)
    hh, ww = max(hh, ww), min(hh, ww)
    count = 0
    while h > hh or w > ww:
        if h > hh:
            h = math.ceil(h / 2)
            count += 1
        if w > ww:
            w = math.ceil(w / 2)
            count += 1
    return count


def solve_2(h, w, hh, ww):
    h, w = max(h, w), min(h, w)
    hh, ww = max(hh, ww), min(hh, ww)
    count = 0
    if h > hh:
        count += math.ceil(math.log2(h) - math.log2(hh))
    if w > ww:
        count += math.ceil(math.log2(w) - math.log2(ww))
    return count


f_count = 0
for i in range(K):
    with open(f"secret/{f_count+6}.in", "w") as in_f, open(
        f"secret/{f_count+6}.ans", "w"
    ) as out_f:
        h, w = (
            random.randint(0, N),
            random.randint(0, N),
        )
        hh, ww = (
            random.randint(0, h),
            random.randint(0, w),
        )

        count_1 = solve_1(h, w, hh, ww)
        count_2 = solve_2(h, w, hh, ww)

        if count_1 != count_2:
            print(f"Found difference {h=}{w=}{hh=}{ww=}\n{count_1=}{count_2=}{i=}")
        print(f"{h} {w}\n{hh} {ww}", file=in_f)
        print(count_1, file=out_f)
        f_count += 1
