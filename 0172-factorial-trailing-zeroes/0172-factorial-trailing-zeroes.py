class Solution(object):
    def trailingZeroes(self, n):
        i,c = 5,0
        while i<=n:
            c+=n//i
            i*=5
        return c