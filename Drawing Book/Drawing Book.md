# Page Turning

## Problem Description

A student has a book with `n` pages. The challenge is to find the minimum number of pages that need to be turned to get to a specific page `p`. A student can start turning pages from the beginning or the end of the book. Note that when they open the book, page 1 is always on the right side.

![Alt text](https://s3.amazonaws.com/hr-challenge-images/0/1481920803-d2b54f38f0-book.png)

 Each subsequent page turn shows two pages (one on the left and one on the right) except possibly the last page.

Given `n` (the number of pages) and `p` (the desired page), determine the minimum number of pages the student needs to turn.

## Example

**Input:**

```
n = 5
p = 3
```

![Alt text](https://s3.amazonaws.com/hr-challenge-images/22564/1467398281-32b69f6fa9-UntitledDiagram4.png)

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

### My First Solution

The fucntion starts by creating an empty list that represents the book. Next it creates another empty list that represents each section of the book, here we will store the page numbers and add them to our book.

Next, the function loops through the number of pages in the book and for every 2 pages it adds those to the section list and then it adds that section to the book list. Afte the loop is done, there will be a list representing each section of the book. The first page always starts on the right side so, the left empty space will be represented by a 0. If the last page is even, there will be an empty page on the right. The function will add a zero in that case to represent the empty space.

Next, the function creates two variables, count_front and count_back. These will be used to keep track of how many page flips it takes to get from the front of the book and how many pages it takes from the back of the book.

Now the funstion loops through the length of sections in the book and when the desired page (p) is found in a section, it will return the number of that section. Then that same process is repeated but with the book sorted in reverse, to represent it starting from the back.

Lastly, the function returns the value of count_front or count_back, depending on which on is smaller.

### Going Over Another Better Solution

The second function is much simpler. It establishes a variable maxFlips which is the maximum amount of pages that will have to be turned to get to a solution.

Then it check if the desired page is 1, if that is the case, then it will return 0 because the shortest route to page one is 0 turned pages from the front. If the desired page is not 1, then two new variables are created to represent the amount of pages needed to be turned to get to the desired page. 

leftToRight starts from the front and it's calculated by integer dividing the desired page (p) by 2. Because each section in the book is made up of two pages, this division works.

rightToLeft is calculated in a different way. Knowing leftToRight and the maxFlips allows to simply subtract leftToRight from maxFlips to get the number of turns that it will take to get to the deisred page (p).

Lastly, we return the minimum value from leftToRight or rightToLeft.

### Reflection

When I started to solve this problem, It was overwhelming the amount of info given. We have a book with a number of pages, and we are counting the number of page turns it takes to get to a desire page from either the front of the back. We return the min value of those two options. 

The way I went about solving it was by first creating the book, represented as a list. This allowed me to visualize the problem and to have the book be manipulated and used easily. After that it was easy to just loop from the back and then the front to see which path takes the shortest.

The reason I did it this way was because it was a way to segment the code in a way that I understood it. First make the book with the number of pages. Then count from the front how many page turns it takes to get there and then front the back an return the smallest value.

The optimal solution while more elegant and simple, it's more of an algorithm. It uses only the crucial information and does not have to loop through the book to count the page turns. It knows that the max number of page turns is the number of pages divided by two, because thats the max number of sections in the book that are possible given the number of pages. It also knows that from front, the number of page turns will be the desired page number divided by 2 because each section is made up of two pages, so half of the desired page number will give you the number of section you have to pass to get to it. Lastly using that info you can calculate the number of page turns from the back by subtracting the number of page turns from the front from the max number of page turns. Lastly, you return the smallest value

This method is one that considers what is the important information and how to get it with making or looping through the book. My solution was O(n) meanwhile the better solution was O(1). In the future, I will try to make sure that I can extract the crucial information first and work from there instead of using all the information.

