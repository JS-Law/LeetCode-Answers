
def countOrders(n):
    slots = 2 * n
    print("available slots: " + str(slots))
    output = 1
    while slots > 0:
        valid_choices = slots * (slots - 1) // 2
        print("Current Valid Choices:" + str(valid_choices))
        output *= valid_choices
        slots -= 2
        print("Current Available Slots: " + str(slots))
    return output % (10 ** 9 + 7)


output = countOrders(3)
print(output)

