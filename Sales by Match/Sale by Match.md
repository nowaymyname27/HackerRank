# Sock Merchant

## Problem Description

You are given a large pile of socks that needs to be paired by color. Your task is to determine how many pairs of socks with matching colors there are.

### Example

Given:  
`n = 7`  
`ar = [1, 2, 1, 2, 1, 3, 2]`

There is one pair of color `1` and one of color `2`. There are three odd socks left, one of each color. The total number of pairs is `2`.

## Function Description

You need to implement the following function:

```python
def sockMerchant(n: int, ar: List[int]) -> int:
    pass
```

### Parameters

- `n` (int): The number of socks in the pile.
- `ar` (List[int]): The colors of each sock.

### Returns

- `int`: The total number of pairs.

## Input Format

- The first line contains an integer `n`, the number of socks represented in `ar`.
- The second line contains `n` space-separated integers, representing the colors of the socks in the pile.

## Constraints

- \(1 \leq n \leq 100\)
- \(1 \leq ar[i] \leq 100\) for \(0 \leq i < n\)

## Sample Input

```
9
10 20 20 10 10 30 50 10 20
```

## Sample Output

```
3
```

### Explanation

There are two pairs of socks with color `10` and one pair of socks with color `20`. Hence, the total number of pairs is `3`.

