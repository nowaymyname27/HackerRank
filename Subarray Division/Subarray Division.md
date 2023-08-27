# Birthday Chocolate

## Problem Description

Lily wants to share a chocolate bar with her friend Ron. The chocolate bar consists of a row of squares, each of which has a number on it. Lily decides to share a contiguous segment of the bar with Ron based on two factors:

1. The length of the segment must match Ron's birth month.
2. The sum of the integers on the squares must equal his birth day.

You need to determine how many ways she can achieve this.

### Example

Given:  
`s = [2, 2, 1, 3, 2]`  
`d = 4` (Ron's birth day)  
`m = 2` (Ron's birth month)

Lily wants to find segments summing to Ron's birth day, `d = 4`, with a length equalling his birth month, `m = 2`. In this case, there are two segments meeting her criteria: `[2, 2]` and `[1, 3]`.

## Function Description

You need to implement the following function:

```python
def birthday(s: List[int], d: int, m: int) -> int:
    pass
```

### Parameters

- `s` (List[int]): The numbers on each square of the chocolate.
- `d` (int): Ron's birth day.
- `m` (int): Ron's birth month.

### Returns

- `int`: The number of ways the bar can be divided according to the rules.

## Input Format

- The first line contains an integer `n`, the number of squares in the chocolate bar.
- The second line contains `n` space-separated integers, representing the numbers on the chocolate squares.
- The third line contains two space-separated integers, `d` and `m`, representing Ron's birth day and his birth month respectively.

## Constraints

- \(1 \leq n \leq 100\)
- \(1 \leq s[i] \leq 5\), where \(0 \leq i < n\)
- \(1 \leq d \leq 31\)
- \(1 \leq m \leq 12\)

