class Solution(object):
    def sortArrayByParity(self, nums):
        return sorted(nums, key=lambda num: num%2)