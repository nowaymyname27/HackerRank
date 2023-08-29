def strings_xor(s, t):
    '''
    Given two strings s and t of equal length, returns their
    bitwise XOR, which is a string of the same length as the inputs
    and contains a 1 where the corresponding bits of s and t differ,
    and a 0 where they are the same.
    
    >>> strings_xor('10101', '00101')
    '10000'
    >>> strings_xor('11001', '01010')
    '10011'
    >>> strings_xor('10000', '10000')
    '00000'
    
    '''
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = '10101'
t = '00101'
print(strings_xor(s, t))


