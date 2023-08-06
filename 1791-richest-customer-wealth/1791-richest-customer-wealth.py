class Solution(object):
    def maximumWealth(self, accounts):
        Max = 0
        for i in range(0,len(accounts)):
            if Max < sum(accounts[i]):
                Max = sum(accounts[i])
        return Max