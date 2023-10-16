class Solution(object):
    def triangularSum(self, nums):
        N = len(nums)
        if N == 1: return nums[0]

        Res, X, Mul = 0, 0, 1
        while X < (N//2):
            Res += (nums[X] + nums[N-X-1]) * Mul
            Mul *= ((N-1)-X)
            Mul //= (X+1)
            X += 1            
        if N % 2 == 1:
            Res += nums[X] * Mul
        return Res % 10
   