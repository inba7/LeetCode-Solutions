class Solution(object):
    def minOperations(self, nums):
        nums.sort()
        unique_len = 1
        ans = len(nums)
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_len] = nums[i]
                unique_len += 1
        
        i, j = 0, 0
        for i in range(unique_len):
            while j < unique_len and nums[j] - nums[i] <= len(nums) - 1:
                j += 1
            ans = min(ans, len(nums) - (j - i))
        return ans