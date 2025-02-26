import math
for _ in range(int(input())):
    s=input()
    if '/' in s:
        x=int(s.split('/')[0])
        print(f"{(math.atan(x/12)*180/math.pi):.1f}")
    else:
        v=float(s)
        print(str(int(12*math.tan(v*math.pi/180)))+'/12')