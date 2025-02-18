## Problem Statement

The following operations on a string are defined:

- Left shift: A single circular rotation of the string where the first character moves to the end and all other characters shift one position to the left.
- Right shift: Same as left shift, but the opposite direction.

For example, the string "abcde" left-shifted would be "bcdea" and right-shifted would be "eabcd".

Given a string and a list of operations, return the resulting string after all shift operations are performed in order.

## Input Format

The first line contains the string to be shifted S.

The second line contains the number of operations to be performed N.

The following lines contain the operations, denoted by an `l` or `r` character, followed by a space, followed by an integer F representing the number of times to shift that direction.

For instance, the following input:

```
roof construction is both a valuable skill and an enjoyable pasttime
3
r 2
l 3
l 1
```

would result in the following output:

```
of construction is both a valuable skill and an enjoyable pasttimero
```

## Output Format

Output a single line containing the shifted string.

## Constraints

0 < |S| < 100,000
0 < N < 100,000
0 < F < 100,000
