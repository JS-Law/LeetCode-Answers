def numberOfSteps(num):
    end_num = -1
    steps = 1
    while end_num == -1:
        if num == 0:
            break
        if num % 2 == 0:
            print("Step " + str(steps) + ") " + str(int(num)) + " is even;"
                  + " divide by 2 and obtain " + str(int(num / 2)))
            num = num / 2
        elif num % 2 != 0:
            print("Step " + str(steps) + ") " + str(int(num)) + " is odd;"
                  + " subtract 1 and obtain " + str(int(num - 1)))
            num -= 1
        steps += 1



numberOfSteps(128444441)