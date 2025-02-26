## Problem Statement

Jane manages all the roofers in Grid City. Roofing projects require many separate tasks to be coordinated in the correct order relative to each other. For example, the task of "Obtain a permit" must be completed before the task "Schedule the work". She knows how long each task will take from start to completion, and she knows which tasks depend on which other tasks to be finished first.

Jane's team is large, meaning that all of a project's unblocked tasks can be worked on concurrently. As soon as all of a task's dependencies are completed, someone on the team will start working on the task. If a task does not depend on any other task, it can be started immediately. She wants to know how long it will take to complete a project, given that each task will be started as soon as its dependencies are completed, each task will take as long as she estimates, and her team is large enough to work on all unblocked tasks concurrently without any increase in time to complete each task.

## Input Format

The first line of input contains two space-separated integers, N and M, the number of tasks and the number of dependencies between tasks, respectively.

The next N lines each contain a single integer T_i, the time it takes to complete task i.

The next M lines each contain two space-separated integers A_i and B_i, where A_i must be completed before B_i is started.

A_i and B_i are 0-indexed.

## Output Format

Output the time it will take to complete the given project as an integer.

## Constraints

0 < N <= 100_000
0 <= M <= 500_000

Each task has a positive integer time of less than 10,000.

It will always be possible to complete a project, so no two tasks will depend on each other to be completed.
