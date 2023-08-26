# Pangram Checker

## Problem Description

A **pangram** is a string that contains every letter of the English alphabet. Your task is to determine whether a given sentence is a pangram. Ignore case and return either `pangram` or `not pangram` as appropriate.

### Example

Given the string:

```
"We promptly judged antique ivory buckles for the next prize"
```

Since the string contains all letters in the English alphabet, the return value should be `pangram`.

## Function Description

Complete the function `pangrams`. It should return the string `pangram` if the input string is a pangram. Otherwise, it should return `not pangram`.

```python
def pangrams(s: str) -> str:
    pass
```

### Parameters:
* `s` (string): a string to test

### Returns:
* string: either `pangram` or `not pangram`

## Input Format

A single line with a string `s`.

### Constraints
* \( 0 < \text{length of } s < 10^3 \)
* Each character of `s`, \( s[i] \), belongs to the set \( \{a - z, A - Z, \text{space}\} \)

## Sample Input & Output

**Sample Input 0**
```
We promptly judged antique ivory buckles for the next prize
```

**Sample Output 0**
```
pangram
```

**Sample Explanation 0**

All of the letters of the alphabet are present in the string.

**Sample Input 1**
```
We promptly judged antique ivory buckles for the prize
```

**Sample Output 1**
```
not pangram
```

**Sample Explanation 1**

The string lacks an `x`.
