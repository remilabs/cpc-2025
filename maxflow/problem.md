## Problem Statement

Remi can assign jobs to certain contractors (who have a capacity of jobs they can do), contractors only service homeowners in their area, homeowners prefer specific contractors, and each homeowner only has one job. Use max flow to find the max number of satisfied customers (jobs completed).

## Input Format

The first line contains 2 space-separated integers N and M, where N is the number of contractors (to be labeled 0 through N-1) and M is the number of homeowners (to be labeled 0 through M-1).

The next N lines each contain a single integer N~i~. Each integer represents the maximum number of homes that contractor _i_ can be assigned to.

The next line contains a single integer C. The next C lines each contain 2 space separated integers A and B where 0 <= A < N and 0 <= B < M. This represents a relationship where homeowner B is close enough to be serviced by contractor A.

The next line contains a single integer H. The next H lines each contain 2 space separated integers A and B where 0 <= A < M and 0 <= B < N. This represents a relationship where homeowner A prefers work on their house to be done by contractor B. Only preferred contractors for each home are allowed to do work for them.

## Output Format

Output a single integer, the maximum number of homes that can be serviced.

## Constraints

1 <= N,M <= 500
0 <= N~i~ <= M
0 <= C <= N^2^
0 <= H <= M^2^

## Time Limit

3 seconds
