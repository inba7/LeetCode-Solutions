class Solution(object):
    def mySqrt(self, x):
        res = x
        while not res * res - x < 1:
            res = (res + x / res) / 2
        return int(res)