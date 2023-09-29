class Solution(object):
    def isMonotonic(self, nums):
        if sorted(nums) == nums or sorted(nums)[::-1] == nums:
            return True
        else:
            return False