class Solution(object):
    def differenceOfSum(self, nums):
        return sum(nums) - sum([int(X) for X in "".join(map(str,nums))])