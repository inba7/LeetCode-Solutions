class Solution(object):
    def rob(self, nums):
        if len(nums) < 2:
            return max(nums)

        DP = [0] * (len(nums))
        DP[0] = nums[0]
        DP[1] = max(nums[0] , nums[1])

        for House in range(2, len(nums)):
            DP[House] = max(DP[House-2]+nums[House], DP[House-1])

        return DP[-1] 