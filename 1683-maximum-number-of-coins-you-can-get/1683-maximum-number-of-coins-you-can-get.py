class Solution(object):
    def maxCoins(self, piles):
        Length = int(2*len(piles)/3)
        piles = sorted(piles)[::-1]
        total = 0
        for i in range(1, Length, 2):
            total += piles[i]
        return total 