#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#

def twoArrays(k, A, B):
    '''
    Given two arrays of integers A and B of length n, determine if there is a way to make A equal to B by
    swapping any pair of elements from array A with a pair of elements from array B. Each swap operation
    swaps the elements at the same index in array A and array B. If it is possible to make A equal to B,
    return "YES", otherwise return "NO".
    
    Example:
    A = [1, 2, 3, 4]
    B = [1, 2, 3, 4]
    k = 5
    
    The arrays are already equal, so no swaps are needed. Thus, we print "YES" on a new line.
    '''
    A.sort()
    B.sort(reverse=True)
    
    # Check for each pair if the sum condition is satisfied
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"


def test():
    test_cases = [
        (1, [0, 1], [0, 2], "YES"),
        # Add more test cases as needed
    ]

    for k, A, B, expected in test_cases:
        result = twoArrays(k, A, B)
        assert result == expected, f"For k={k}, A={A}, and B={B}: expected {expected} but got {result}"
        print(f"Test passed for k={k}, A={A}, and B={B}")

if __name__ == '__main__':
    test()