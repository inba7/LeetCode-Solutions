class Solution(object):
    def rearrangeArray(self, nums):
        N = len(nums)
        Res = [0] * N
        Pos, Neg = 0, 1
        for n in nums:
            if n < 0:
                Res[Neg] = n
                Neg += 2
            else:
                Res[Pos] = n
                Pos += 2
        return Res