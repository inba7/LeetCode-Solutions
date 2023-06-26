class Solution(object):
    def countBits(self, n):
        d = [0]
        for item in range(1, n+1):
            d.append(d[item >> 1] + (item & 1))
        return d