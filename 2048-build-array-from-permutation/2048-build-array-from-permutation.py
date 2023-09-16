class Solution(object):
    def buildArray(self, nums):
        ans = list()
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans