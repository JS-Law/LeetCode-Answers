def maximumWealth(self, accounts):
    mostWealth = 0
    wealth = 0
    for i in range(len(accounts)):
        wealth = sum(accounts[i])
        mostWealth = max(mostWealth, wealth)
    return mostWealth
