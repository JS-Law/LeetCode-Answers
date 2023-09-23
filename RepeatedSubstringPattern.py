def repeatedSubstringPattern(s):
    print(s + s)
    t = s+s[1: -1]
    print(t)
    return s in (s + s)[1:-1]

    # r_string = s[::-1]
    # if r_string == s:
    #     print(r_string, s)
    #     return False
    # else:
    #     print(r_string, s)
    #     return True
    #
    #

# s = "ab"
s = "abracadabra"

output = repeatedSubstringPattern(s)
print(output)

























