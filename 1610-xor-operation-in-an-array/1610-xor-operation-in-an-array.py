class Solution(object):
    def xorOperation(self, n, start):
        XOR = 0
        while n > 0:
            XOR ^= start
            start += 2
            n -= 1
        return XOR