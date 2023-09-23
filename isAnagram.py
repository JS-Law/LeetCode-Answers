def isAnagram(s, t):
    s_count = {}
    t_count = {}
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1

    if t_count == s_count:
        return True
    else:
        return False
# s = "anagram"
# t = "nagaram"

s = "rat"
t = "car"

op = isAnagram(s,t)
    # r_string = s[::-1]
    # print(r_string)
    # if s == r_string:
    #     return True
    #     print("True")
    # else:
    #     print("True")
    #     return False
