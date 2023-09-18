def strStr(haystack, needle):
    n_length = len(needle)
    for i in range(len(haystack) - n_length + 1):
        if haystack[i:i + n_length] == needle:
            print(i)
            return i
    return -1
haystack = "sadbutsad"
needle = "sad"
output = strStr(haystack, needle)












    # i = j = 0
    # h_stack = {}
    # n_stack = {}
    # for char in  haystack:
    #     h_stack[char] = h_stack.get(char, 0) + 1
    # for char in needle:
    #     n_stack[char] = n_stack.get(char, 0) + 1
    # print(h_stack)
    # print(n_stack)
