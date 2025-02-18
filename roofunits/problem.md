## Problem Statement

Chuck the roofer has to convert between lots of different units during his day job. One example is the different ways his crew measures how steep a roof is. There are two main methods for doing this in Chucks crew.

1. Use a measuring tool to get the angle of the roof off of horizontal in degrees (e.g. 15 degrees off horizontal)
2. Use a measuring tool to find how much the roof rises over 12 inches of horizontal run (e.g. 5 inches of rise for 12 inches of run)

This second method is expressed in the form X/12 where X is the height the roof rises in inches over 12 inches of horizontal run.

Chuck needs to convert from one form to the other in order to coordinate between his crews.

## Input Format

The first line contains a number N which is the number of queries that you will process

The following N lines each contains a query that gives the pitch of the roof in one of the two units used

- If the line contains a single floating point number x, it will be the pitch of the roof in degrees

- If the line contains two integers separated by a slash (X/12), it will be the pitch of the roof in rise/run format

## Output Format

For each query, convert the pitch to the other unit.

For example, if the query looks like the following

```txt
11/12
```

You will output

```txt
42.5
```

And if the query looks like

```txt
33.3
```

You will output

```txt
7/12
```

For degrees, round any floating point answers to the nearest tenth in your output

For rise/run, truncate any floating point answers down to an integer

## Constraints

0 < N <= 10^5

For pitch measurements in degrees:

0.0 <= X < 90.0

For pitch measurements in rise/run (X/12):

0 <= X <=1000
