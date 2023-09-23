def plusOne(digits):
    print(digits)
    res = int("".join(map(str, digits)))
    print(res)
    res += 1
    res = [int(x) for x in str(res)]
    print(res)


digits = [2, 0, 1, 9]
output = plusOne(digits)
print(output)
