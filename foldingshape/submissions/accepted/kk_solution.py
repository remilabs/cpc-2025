import math


def solve():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
    count = 0
    while h > hh:
        h = math.ceil(h / 2)
        count += 1
    while w > ww:
        w = math.ceil(w / 2)
        count += 1
    return count


print(solve())
