class Solution(object):
    def countPairs(self, nums, target):
        Count = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] < target:
                    Count+=1
        return Count