def canMakeArithmeticProgression(arr):
    s = sorted(arr)
    diff = s[0] - s[1]
    for i in range(2, len(s)):
        if diff != s[i - 1] - s[i]:
            return False
    return True


# It first sorts the input list arr using the sorted function and stores the sorted result in the variable s. Sorting
# the array is not strictly necessary for checking if it forms an arithmetic progression, but it makes it easier to
# check if the difference between consecutive elements is constant.
#
# It calculates the common difference by subtracting the second element from the first element (diff = s[0] - s[1]).
# This is the difference that should remain constant throughout the progression.
#
# It then iterates through the sorted array s starting from the third element (i starts from 2) and checks if the
# difference between the previous element (s[i-1]) and the current element (s[i]) is equal to the common
# difference (diff). If at any point this condition is not met, the function returns False, indicating that the input
# list does not form an arithmetic progression.
#
# If the loop completes without returning False, it means that all the differences between consecutive elements are
# equal to the common difference, and the function returns True, indicating that the input list forms
# an arithmetic progression.