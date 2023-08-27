def birthday(s, d, m):
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