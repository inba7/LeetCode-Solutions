class Solution(object):
    def xorOperation(self, n, start):
        XOR = 0
        for num in range(0,n):
            XOR ^= start + (num*2)
        return XOR