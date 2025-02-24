## Problem Statement

Chuck the roofer has to convert between lots of different units during his day job. One example is how his crew measures how steep a roof is. There are two main methods for doing this in Chuck's crew.

1. Use a measuring tool to get the angle of the roof off of horizontal in degrees (e.g. 15 degrees off horizontal)
2. Use a measuring tool to find how much the roof rises over 12 inches of horizontal run (e.g. 5 inches of rise for 12 inches of run)

This second method is expressed as X/12 where X is the height the roof rises in inches over 12 inches of horizontal run.

Chuck needs to convert from one form to the other to coordinate between his crews.

## Input Format

The first line contains an integer, N, which is the number of queries.

The following N lines each contain either a single floating point number or a fraction, which is the query to process. If a query contains a slash ( / ), it is a fraction and needs to be converted to the number of degrees off of horizontal. Otherwise, it needs to be converted to the form X/12.

## Output Format

For each query, output the converted pitch on a single line.

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

For rise/run, truncate any floating point answers to an integer.

## Constraints

0 < N <= 10^5

For pitch measurements in degrees:

0.0 <= X < 90.0

For pitch measurements in rise/run (X/12):

0 <= X <=1000
