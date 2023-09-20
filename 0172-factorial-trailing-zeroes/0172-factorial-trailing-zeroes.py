class Solution(object):
    def trailingZeroes(self, n):
        Inc, Count = 5, 0
        while Inc<=n:
            Count += n//Inc
            Inc*=5
        return Count

        i,c = 5,0
        while i<=n:
            c+=n//i
            i*=5
        return c