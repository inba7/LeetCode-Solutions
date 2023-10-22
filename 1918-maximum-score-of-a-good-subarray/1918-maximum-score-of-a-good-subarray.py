class Solution(object):
    def maximumScore(self, nums, k):
        N, MinVal = len(nums), nums[k]
        Left = Right = k
        Res = 0
        
        while Left >= 0 or Right < N:
            while Left >= 0 and nums[Left] >= MinVal: Left -= 1
            while Right < N and nums[Right] >= MinVal: Right += 1
            Res = max(Res, MinVal*(Right-Left-1))
            MinVal = max(nums[Left] if Left >= 0 else -float('inf'), nums[Right] if Right < N else -float('inf'))
        return Res