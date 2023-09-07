# Tower Breakers Game

## Problem Description

Two players engage in a game of Tower Breakers. The game rules are:

1. There are `n` towers initially.
2. Every tower has a height of `m`.
3. Players play alternately; Player 1 starts.
4. In each turn, a player can choose a tower of height `x` and reduce its height to `y`, where `1 <= y < x` and `y` is a divisor of `x`.
5. The player unable to make a move loses.

Given `n` and `m`, determine the winning player. If Player 1 wins, return `1`. If Player 2 wins, return `2`.

### Example

Given:  
`n = 2`  
`m = 6`

Player 1 can:
- Reduce a tower's height from 6 to 3 since 6 modulo 3 = 0.
- Reduce a tower's height from 5 to 1.

Player 1 chooses the first option. Towers are now 3 and 6 units tall. Player 2 follows suit, making towers 3 units each. Player 1 then has only one move left, reducing a tower from 3 to 1. Player 2 does the same. Now, both towers are 1 unit tall, and Player 1 has no moves left, so Player 2 wins. Return `2`.

## Function Description

Implement the following function:

```python
def towerBreakers(n: int, m: int) -> int:
    pass
```

### Parameters

- `n` (int): The number of towers.
- `m` (int): The initial height of each tower.

### Returns

- `int`: `1` if Player 1 wins, `2` otherwise.

## Input Format

- The first line contains an integer `t`, the number of test cases.
- The next `t` lines each describe a test case with two space-separated integers, `n` and `m`.

## Constraints

- \(1 \leq t \leq 100\)
- \(1 \leq n, m \leq 10^6\)

## Sample Input

```
2
2 2
1 4
```

## Sample Output

```
2
1
```

### Explanation

In the first test:
Player 1 reduces one tower to height 1. Player 2 does the same. With both towers at height 1, Player 1 can't play. Player 2 wins.

In the second test:
Only one tower with height 4. Player 1 reduces it to 1. Player 2 has no moves. Player 1 wins.
