def check(arr):
    N = len(arr)
    inc = True
    dec = True

    # Loop to check if array is increasing
    for i in range(0, N - 1):

        # To check if array is not increasing
        if arr[i] > arr[i + 1]:
            inc = False

    # Loop to check if array is decreasing
    for i in range(0, N - 1):

        # To check if array is not decreasing
        if arr[i] < arr[i + 1]:
            dec = False

    # Pick one whether inc or dec
    return inc or dec


# The provided Python function check(arr) is designed to check whether the input array arr is either strictly
# increasing or strictly decreasing. It does this by iterating through the elements of the array and setting flags
# (inc and dec) to True or False accordingly. Finally, it returns True if either inc or dec is True, indicating that
# the array is either increasing or decreasing, and returns False if neither is True, indicating that the array is
# neither strictly increasing nor strictly decreasing.

# Here's a step-by-step explanation of how the function works:

# It calculates the length of the input array arr and assigns it to the variable N.

# It initializes two boolean variables, inc and dec, to True. These variables will be used to keep track of whether
# the array is increasing or decreasing.

# It iterates through the array from index 0 to N-2 (inclusive) using a for loop.

# In the first loop, it checks if the current element arr[i] is greater than the next element arr[i+1].
# If this condition is true, it means the array is not strictly increasing, so it sets inc to False.

# It then enters a second loop, which is essentially the same as the first loop, but it checks if the current
# element arr[i] is less than the next element arr[i+1]. If this condition is true, it means the array is not strictly
# decreasing, so it sets dec to False.

# Finally, it returns the result of the logical OR operation between inc and dec. If either inc or dec is True,
# it means the array is either strictly increasing or strictly decreasing, so the function returns True. If both
# inc and dec are False, it means the array is neither strictly increasing nor strictly decreasing, and the
# function returns False.