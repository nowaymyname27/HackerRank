from typing import List

def birthday(s, d, m):
    

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