import math

def solve():
    h, w = map(int, input().split())
    hh, ww = map(int, input().split())
    count = 0
    if h > hh:
        count += math.ceil(math.log2(h) - math.log2(hh))
    if w > ww:
        count += math.ceil(math.log2(w) - math.log2(ww))
    hh,ww=ww,hh
    count2 = 0
    if h > hh:
        count2+= math.ceil(math.log2(h) - math.log2(hh))
    if w > ww:
        count2 += math.ceil(math.log2(w) - math.log2(ww))
    return min(count,count2)

print(solve())
