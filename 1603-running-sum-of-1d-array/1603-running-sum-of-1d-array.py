class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            Temp = nums[i]
            nums[i] = nums[i-1] + Temp
        return nums