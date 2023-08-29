
def sockMerchant(n, ar):
    """
    There is a large pile of socks that must be paired by color.
    Given an array of integers representing the color of each sock,
    determine how many pairs of socks with matching colors there are.
    
    Example:
    n = 7
    ar = [1, 2, 1, 2, 1, 3, 2]
    
    There is one pair of color 1 and one of color 2.
    There are three odd socks left, one of each color.
    The number of pairs is 2.
    """
    checker = []
    count = 0
    for num in ar:
        if num in checker:
            checker.remove(num)
            count += 1
        else:
            checker.append(num)
    return count
            


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
