class Solution(object):
    def longestOnes(self, nums, k):
        Left = 0
        for Right in range(len(nums)):
            k-=(1-nums[Right])
            if k < 0:
                k+=(1-nums[Left])
                Left += 1
        return Right-Left+1