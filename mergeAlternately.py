def solve(word1, word2):
    i = j = 0
    result = ""
    while i < len(word1) and j < len(word2):
        result += word1[i] + word2[j]
        print("     ", word1[i])
        print("     ", word2[j])
        i += 1
        j += 1
        print(i, "i")
        print(j, "j")
        print(result)

    while i < len(word1):
        result += word1[i]
        i += 1
        print(i, "i")
    while j < len(word2):
        result += word2[j]
        j += 1
        print(j, "j")
    return result

t = "major"
s = "general"
print(solve(s, t))