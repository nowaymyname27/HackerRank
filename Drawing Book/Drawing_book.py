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
    divisions = n / 2
    divisions = math.ceil(divisions)
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
    for turn_page in range(divisions):
        if p in book[turn_page]:
            count_front = turn_page
    book.sort(reverse=True)
    for turn_page in range(divisions):
        if p in book[turn_page]:
            count_back = turn_page
    if count_front < count_back:
        return count_front
    else:
        return count_back
    
def main():
    print(pageCount(6, 5))

main()