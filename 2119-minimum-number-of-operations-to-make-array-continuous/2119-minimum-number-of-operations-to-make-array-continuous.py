class Solution(object):
    def minOperations(self, nums):
        N = len(nums)
        nums = sorted(set(nums))

        Res = j = 0
        for Idx, Val in enumerate(nums):
            if Val - nums[j] >= N:
                j += 1
            Res = max(Res, Idx-j+1)
        
        return N-Res