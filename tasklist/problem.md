## Problem Statement

Jane manages all the roofers in Grid City. To get the work done on someones roof, there are lots of tasks that need to be coordinated such as pulling permits or scheduling crew arrivals. Some of these tasks need to happen before others, but often Jane's team can work on more than one task at a time. She knows how long it takes her team to do each task (she's been doing this for a while), and she knows which tasks depend on which other tasks. She wants to know how long it will take to finish all the tasks if she is optimal about delegating the tasks out to her team. She can't start work on a task until all its dependencies are completed.

## Input Format

The first line of input contains two integers N and M

N is the number of tasks and M is the number of dependencies between tasks.

The next N lines each contain a single integer T_i, the time it takes to complete task i.

The next M lines each contain two integers A_i and B_i, which means that task A_i must be completed before task B_i can start.

A_i and B_i are 0-indexed.

## Output Format

Output a single integer, which is the minimum time it will take to complete all the tasks if Jane manages her team optimally.

## Constraints

0 < N <= 10_000
0 <= M <= 10_000

Each task has an integer time that satisfies

0 < T_i <= 10_000

There will be no cycles in the graph of task dependencies.
