class Solution(object):
    def minFlips(self, a, b, c):
        Count = 0
        while a or b or c:
            A = a & 1
            B = b & 1
            C = c & 1
            if C == 0:
                Count += A + B
            else:
                Count += (A | B) ^ 1
            a >>= 1
            b >>= 1
            c >>= 1
        return Count