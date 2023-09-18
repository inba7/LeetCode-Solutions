class Solution(object):
    def maxCoins(self, piles):
        piles.sort()
        Sum = 0
        N = len(piles)
        for n in range(N-1, int(N/3), -2):
            Sum += piles[n-1]
        return Sum