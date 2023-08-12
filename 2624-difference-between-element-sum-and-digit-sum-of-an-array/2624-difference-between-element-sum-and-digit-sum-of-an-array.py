class Solution(object):
    def differenceOfSum(self, nums):
        Sum1 = sum(nums)
        Sum2 = 0
        for num in nums:
            while num>0:
                Sum2+=(num%10)
                num//=10
        return abs(Sum1-Sum2)