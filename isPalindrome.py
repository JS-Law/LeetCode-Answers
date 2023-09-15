def isPalindrome(x):
    x = str(x)
    reverse_int = x[::-1]
    if x == reverse_int:
        return True, print("True")
    else:
        return False


isPalindrome(343)