class Solution(object):
    def maxProfit(self, prices, fee):
        Profit, Pre_min = 0, prices[0]

        for p in prices[1:]:
            if p > Pre_min + fee:
                Profit += p - Pre_min - fee
                Pre_min = p - fee
            else:
                Pre_min = min(Pre_min, p)
        
        return Profit