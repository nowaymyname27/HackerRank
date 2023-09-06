#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

import math

def pageCount(n, p):
    '''
    First iteration of this solution
    '''
    book = []
    section = []
    for page in range(n+1):
        section.append(page)
        if len(section) == 2:
            book.append(section)
            section = []
    if section is not []:
        section.append(0)
        book.append(section)
    count_front = 0
    count_back = 0
    for turns in range(len(book)):
        if p in book[turns]:
            count_front = turns
    book.sort(reverse=True)
    for turns in range(len(book)):
        if p in book[turns]:
            count_back = turns
    return min(count_back, count_front)
    
def pageCount2(n, p):
    # Someone else's solution
    maxFlips = int(n / 2)
    
    if p == 1:
        return 0
    else:
        leftToRight = int(p / 2)
        rightToLeft = maxFlips - leftToRight
        return min(leftToRight, rightToLeft)
    
def main():
    print(pageCount(6, 5))
    print(pageCount2(10, 10))

main()