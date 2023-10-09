class Solution(object):
    def maxProfit(self, prices, fee):
        Pos =- prices[0]
        Profit = 0
        N = len(prices)
        for i in range(1, N):
            Pos = max(Pos, Profit-prices[i])
            Profit = max(Profit, Pos + prices[i] - fee)

        return Profit