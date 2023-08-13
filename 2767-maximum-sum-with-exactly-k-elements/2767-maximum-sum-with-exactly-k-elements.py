class Solution(object):
    def maximizeSum(self, nums, k):
        Max = max(nums)*k
        for i in range(k):
            Max+=i
        return Max