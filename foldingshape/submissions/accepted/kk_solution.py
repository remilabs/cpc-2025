import math


def solve():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
    ch,cw = h,w
    count = 0
    while h > hh or w > ww:
        if h > hh:
            h = math.ceil(h / 2)
            count += 1
        if w > ww:
            w = math.ceil(w / 2)
            count += 1
    h, w = cw, ch
    count2 = 0
    while h > hh or w > ww:
        if h > hh:
            h = math.ceil(h / 2)
            count2 += 1
        if w > ww:
            w = math.ceil(w / 2)
            count2 += 1
    return min(count,count2)


print(solve())
