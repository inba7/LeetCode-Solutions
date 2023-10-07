class Solution(object):
    def rob(self, nums):
        Rob1, Rob2 = 0, 0

        for i in nums:
            Temp = max(i+Rob1, Rob2)
            Rob1 = Rob2
            Rob2 = Temp
        return Rob2