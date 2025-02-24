## Problem Statement

Chuck is driving his truck through Grid City to reach his next roofing job. However, due to a broken turn signal, he can only turn right. As he waits in traffic, he wonders how many different routes he can take to reach his destination while following these rules:

1. Each turn must bring him strictly closer to his destination than the previous turn. 
2. His first turn must also move him closer to the destination than his starting position.
3. Some intersections are blocked due to Grid City's ongoing Pi Day parade. Chuck cannot drive through or turn at these intersections.

The city is modeled as a coordinate plane, where each intersection is represented by integer coordinates. Chuck's destination is always at the origin (0, 0).

Your task is to calculate the number of valid paths Chuck can take to his destination.


## Input Format

The first line of input contains three integers:

X Y N — Chuck's starting coordinates (X, Y) and the number of blocked intersections (N).

The next N lines each contain two integers:

x_i y_i — The coordinates of the i-th blocked intersection.

It is guaranteed that Chuck’s starting location will never be a blocked intersection. Assume that Chuck's truck is oriented in whichever direction makes this task possible. For example, if he is in the first quadrant, his truck is pointed south, in the direction of the negative Y-axis. If he begins in the second quadrant, he starts out driving east, in the direction of the positive X-axis.

## Output Format

Output a single integer, which is the number of ways that Chuck can drive to his next job. Since this number can get quite large, output the answer modulo 1,000,000,007. It is guaranteed that there will be at least one way for Chuck to get to his destination.

## Constraints

The constraints of X, Y, N, and each x_i, y_i are 0 < |X|, |Y|, |x_i|, |y_i| <= 150, 0 < N <= 10. For clarity, |X| denotes the absolute value of X.
