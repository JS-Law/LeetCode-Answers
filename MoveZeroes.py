def move_to_end(nums):
    j = 0
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1
        print(nums)
    print("second loop\n")
    for x in range(j, len(nums)):
        nums[x] = 0
        print(nums)
    return nums


nums = [0, 1, 0, 3, 12]

print(move_to_end(nums))  # should print [1, 2, 4, 5, 3]
# This code is contributed by Edula Vinay Kumar Reddy
