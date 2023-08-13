class Solution(object):
    def maximizeSum(self, nums, k):
        Max = max(nums)*k + (k-1)*(k)/2
        return Max