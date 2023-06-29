class Solution(object):
    def largestAltitude(self, gain):
        s, res = 0, 0
        for h in gain:
            s += h
            res = max(res, s)
        return res