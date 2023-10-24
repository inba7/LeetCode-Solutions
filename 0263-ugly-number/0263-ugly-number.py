class Solution(object):
    def isUgly(self, N):
        if N <= 0: return False
        
        for num in [2, 3, 5]:
            while N % num == 0:
                N = N // num
        return N == 1