from typing import List

def sockMerchant(n, ar):
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
