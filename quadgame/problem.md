## Problem Statement

After a long day at work, Chuck decides to relax and play a single-player game that he calls Quad Game. This game is played with straight rods of negligible diameters and varying lengths. He picks two arbitrary rods and places them at a right angle, so one end of a rod is touching the end of another rod. He then must pick two other rods out of a pile and lay them out to form a quadrilateral that satisfies the following conditions:

- The quadrilateral must have at least two right angles, including the initial right angle formed by the first two rods.
- The quadrilateral must have a positive area (i.e., it must be a valid, non-degenerate shape).
- The perimeter of the quadrilateral must equal the sum of the lengths of the four rods used.
- The object of Quad Game is to minimize this perimeter while satisfying all constraints.

Your task is to write a program that determines the smallest possible perimeter of such a quadrilateral so that Chuck can check his answer.


## Input Format

The first line of input will contain one integer, N, the number of rods.

- The first line contains a single integer N, the number of rods.
- The second line contains N space-separated integers representing the lengths of the rods.
  - The first two integers correspond to the rods that form the initial right angle.
  - The remaining N−2 integers represent the available rods for completing the quadrilateral.

## Output Format

Output a single integer, the smallest perimeter of a quadrilateral that can be formed with the above constraints. If no valid quadrilateral can be formed, output -1.

## Constraints

4 <= N <= 100,000
Each rod will have a length greather than zero and no more than 100,000.
