
# Two Arrays and Permutations

## Problem Description

Given two n-element arrays of integers, `A` and `B`, you are required to permute them into `A'` and `B'` such that the following relation holds for all `i` where `0 ≤ i < n`:

\[ A'[i] + B'[i] ≥ k \]

There will be `q` queries, each consisting of the arrays `A`, `B`, and an integer `k`. For each query, you need to determine if there exists some permutation `A'`, `B'` satisfying the above relation.

### Example

Given:  
`A = [0, 1]`  
`B = [0, 2]`  
`k = 1`

A valid `A'`, `B'` can be `A' = [1, 0]` and `B' = [0, 2]`:  
`1 + 0 > 1` and `0 + 2 ≥ 1`. Thus, the answer is `YES`.

## Function Description

You need to implement the following function:

```python
def twoArrays(k: int, A: List[int], B: List[int]) -> str:
    pass
```

### Parameters

- `k` (int): An integer.
- `A` (List[int]): An array of integers.
- `B` (List[int]): An array of integers.

### Returns

- `str`: A string value either "YES" or "NO".

## Input Format

- The first line contains an integer `q`, denoting the number of queries.
  
For the next `q` sets of 3 lines:

- The first line contains two space-separated integers `n` and `k`. `n` represents the size of both arrays `A` and `B`, and `k` is the relation variable.
- The second line contains `n` space-separated integers representing the elements of array `A`.
- The third line contains `n` space-separated integers representing the elements of array `B`.

## Constraints

- \(1 ≤ q ≤ 10\)
- \(1 ≤ n ≤ 1000\)
- \(1 ≤ k < 10^9\)
- \(0 ≤ A_i, B_i < 10^9\)
