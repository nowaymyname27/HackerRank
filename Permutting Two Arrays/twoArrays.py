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
    # Sort A in ascending order and B in descending order
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