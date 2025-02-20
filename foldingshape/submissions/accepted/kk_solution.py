import math


def solve():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
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
        h, w = max(h, w), min(h, w)
    return count


print(solve())
