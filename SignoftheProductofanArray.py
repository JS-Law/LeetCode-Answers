def arraySign(nums):
    def signFunc(x):
        if x > 1:
            return 1
        elif x < 0:
            return -1
        elif x == 0:
            return 0

    product = 1
    for num in nums:
        product *= num
    print(product)
    return signFunc(product)


nums = [-1,-2,-3,-4,3,2,1]
arraySign(nums)