import math

n = int(input())


def deg_to_rise_run(deg):
    return 12 * math.tan(deg * math.pi / 180)


def rise_run_to_deg(rise):
    return math.atan(rise / 12) * 180 / math.pi


for _ in range(n):
    line = input()
    # rise/run
    if "/" in line:
        x, _ = line.split("/")
        x = int(x)
        deg = rise_run_to_deg(x)
        print(f"{deg}")
    # degrees
    else:
        x = float(line)
        rise = deg_to_rise_run(x)
        print(f"{rise}/12")
