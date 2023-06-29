class Solution(object):
    def largestAltitude(self, gain):
        s = 0
        res = 0
        for h in gain:
            s += h
            res = max(res, s)

        return res