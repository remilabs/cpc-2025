## Problem Statement

Remi works hard to make sure roofing contractors have work to do and homeowners have someone to work on their roof. Contractors have a maximum number of jobs they're able to do at once. Contractors are also limited to homes that are located within their market, and homeowners have specific contractors they prefer to work with. If a prefered contractor is able to do work on a home, that customer is satisfied.

Assuming all homeowners have work to be done on their roof, what's the maximum number of satisfied customers Remi is able to achieve based on these constraints?

## Input Format

The first line contains 2 space-separated integers N and M, where N is the number of contractors (to be labeled 0 through N-1) and M is the number of homeowners (to be labeled 0 through M-1).

The next N lines each contain a single integer N<sub>i</sub>. Each integer represents the maximum number of homes that contractor _i_ can be assigned to.

The next line contains a single integer C. The next C lines each contain 2 space separated integers A and B where 0 <= A < N and 0 <= B < M. This represents a relationship where homeowner B is close enough to be serviced by contractor A.

The next line contains a single integer H. The next H lines each contain 2 space separated integers A and B where 0 <= A < M and 0 <= B < N. This represents a relationship where homeowner A prefers work on their house to be done by contractor B.

## Output Format

Output a single integer, the maximum number of homes that can be serviced.

## Constraints

1 <= N,M <= 500<br/>
0 <= N<sub>i</sub> <= M<br/>
0 <= C <= N<sup>2</sup><br/>
0 <= H <= M<sup>2</sup><br/>

## Time Limit

3 seconds
