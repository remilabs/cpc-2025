import math

def solve():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
    h, w = max(h, w), min(h, w)
    hh, ww = max(hh, ww), min(hh, ww)
    count = 0
    if h > hh:
        count += math.ceil(math.log2(h) - math.log2(hh))
    if w > ww:
        count += math.ceil(math.log2(w) - math.log2(ww))
    return count

print(solve())
