def birthday(s, d, m):
    '''
    s: an array of integers, the numbers on each of the squares of chocolate
    d: an integer, Ron's birth day
    m: an integer, Ron's birth month
    
    Returns an integer denoting the number of ways Lily can divide the chocolate bar.
    
    Example:
    s = [2, 2, 1, 3, 2]
    d = 4
    m = 2
    
    Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his birth month, m = 2.
    
    In this case, there are two segments meeting her criteria: [2, 2] and [1, 3].
    
    '''
    count = 0
    n = len(s)
    
    # Loop over each starting point
    for start in range(n - m + 1):  # Ensure we have enough squares left for a full segment
        end = start + m
        if sum(s[start:end]) == d:  # Check if the sum of segment equals d
            count += 1

    return count
    
    

# Test function
def test():
    test_cases = [
        ([2, 2, 1, 3, 2], 4, 2, 2),
        # Add more test cases as needed
    ]

    for s, d, m, expected in test_cases:
        result = birthday(s, d, m)
        assert result == expected, f"For s={s}, d={d}, and m={m}: expected {expected} but got {result}"
        print(f"Test passed for s={s}, d={d}, and m={m}")

if __name__ == '__main__':
    test()