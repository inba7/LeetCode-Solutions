class Solution(object):
    def combinationSum4(self, nums, target):
        DP = [0] * (target + 1)
        DP[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    DP[i] += DP[i - num]        
        return DP[target]