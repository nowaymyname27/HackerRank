# Page Turning

## Problem Description

A student has a book with `n` pages. The challenge is to find the minimum number of pages that need to be turned to get to a specific page `p`. A student can start turning pages from the beginning or the end of the book. Note that when they open the book, page 1 is always on the right side. Each subsequent page turn shows two pages (one on the left and one on the right) except possibly the last page if the total number of pages is odd.

Given `n` (the number of pages) and `p` (the desired page), determine the minimum number of pages the student needs to turn.

## Example

**Input:**

```
n = 5
p = 3
```

**Output:**

```
1
```

**Explanation:**

If the student opens the book and turns one page, they'll see pages 2 and 3. This is the minimum number of pages to turn to get to page 3. Alternatively, if the student opens the book from the back, they'd also need to turn one page to get to page 3. Therefore, the minimum is 1 page turn.

## Function Signature

```python
def pageCount(n: int, p: int) -> int:
```

### Input

1. An integer `n` representing the total number of pages in the book. (1 ≤ n ≤ 10^5)
2. An integer `p` representing the desired page number. (1 ≤ p ≤ n)

### Output

Return an integer representing the minimum number of page turns required to get to page `p`.
