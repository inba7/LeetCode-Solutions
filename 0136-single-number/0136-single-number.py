class Solution(object):
    def singleNumber(self, nums):
        Num = set(nums)
        for i in Num:
            if nums.count(i) == 1:
                return i