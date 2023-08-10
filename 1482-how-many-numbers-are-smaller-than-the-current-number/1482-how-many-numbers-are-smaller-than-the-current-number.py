class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        Out = []
        Temp = sorted(nums)
        for num in nums:
            Out.append(Temp.index(num))
        return Out