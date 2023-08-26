import string

def pangrams(s):
    alphabet_list = list(string.ascii_lowercase)
    s = s.lower()
    for letter in s:
        if letter in alphabet_list:
            alphabet_list.remove(letter)
        
    if alphabet_list == []:
        return 'pangram'
    else:
        return 'not pangram'
    

# Test function
def test():
    test_cases = [
        ("We promptly judged antique ivory buckles for the next prize", "pangram"),
        ("The quick brown fox jumps over the lazy dog", "pangram"),
        ("Hello World", "not pangram"),
        # Add more test cases as needed
    ]

    for s, expected in test_cases:
        result = pangrams(s)
        assert result == expected, f"For: {s}, expected: {expected} but got: {result}"
        print(f"Test passed for: '{s}'")

if __name__ == '__main__':
    test()
