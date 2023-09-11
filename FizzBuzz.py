def fizzBuzz(n):
    fizzList = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizzList.append("FizzBuzz")
        elif i % 3 == 0:
            fizzList.append("Fizz")
        elif i % 5 == 0:
            fizzList.append("Buzz")
        elif i % 5 != 0 and i % 3 != 0:
            fizzList.append(str(i))
    print(fizzList)


fizzBuzz(2)
