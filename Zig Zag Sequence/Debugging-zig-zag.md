# Debugging: Zig Zag Sequence

## Problem Description

In this challenge, your task is to debug existing code to successfully execute all provided test cases. Given an array of \( n \) distinct integers, the goal is to transform the array into a zig-zag sequence.

A sequence is called a zig-zag sequence if:
- The first \( k \) elements in the sequence are in increasing order, and
- The last \( k \) elements are in decreasing order,

where \( k = \frac{n + 1}{2} \).

The objective is to find the lexicographically smallest zig-zag sequence for the given array.

**Note**: You can modify at most three lines in the given code. You cannot add or remove lines of code.

## Input Format

- The first line contains \( t \), the number of test cases.
- Each test case starts with a line containing an integer \( n \), denoting the number of array elements.
- The next line of each test case contains \( n \) space-separated integers, the elements of array \( a \).

### Constraints

- \( 1 \leq t \leq 20 \)
- \( 1 \leq n < 10000 \) (Note: \( n \) is always odd)
- \( 1 \leq a_i < 10^9 \)

## Output Format

For each test case, print the elements of the transformed zig-zag sequence in a single line.

## Example

### Input

```
1
5
2 3 5 1 4
```

### Output

```
1 4 5 3 2
```

### Explanation

The array can be permuted as `[1, 4, 5, 3, 2]`, which is a zig-zag sequence. The first 3 numbers are in increasing order and the last 2 numbers are in decreasing order.
