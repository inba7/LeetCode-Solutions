class Solution(object):
    def numIdenticalPairs(self, nums):
        Count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    Count += 1
        return Count