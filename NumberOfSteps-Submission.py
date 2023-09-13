def numberOfSteps(num):
    steps = 0
    while num:
        if num%2==0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps


output = numberOfSteps(128444441)
print(output)