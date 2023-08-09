class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        Count = 0
        for stone in stones:
            if stone in jewels:
                Count += 1
        return Count