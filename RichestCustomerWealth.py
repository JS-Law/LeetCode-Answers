def maximumWealth(accounts):
    mostWealth = 0
    wealth = 0
    for i in range(len(accounts)):
        wealth = sum(accounts[i])
        print("Current customer wealth: " + str(i) + " "+ str(wealth))
        mostWealth = max(mostWealth, wealth)
    return "Customer index " + str(i) + " has the highest wealth with a value of " + str(mostWealth)


accounts = [[9, 5, 3], [3, 4, 5], [9, 6, 8]]
mostWealth = maximumWealth(accounts)
print(mostWealth)