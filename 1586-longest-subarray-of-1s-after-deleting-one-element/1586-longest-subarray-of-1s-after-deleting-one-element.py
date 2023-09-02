class Solution(object):
    def longestSubarray(self, nums):
        Prev, Curr, Ans = 0, 0, 0
        for i in nums:
            if i == 1:
                Curr += 1
            else:
                Ans = max(Ans, Curr + Prev)
                Prev = Curr
                Curr = 0
        Ans = max(Ans, Curr + Prev)

        return Ans-1 if Ans == len(nums) else Ans        