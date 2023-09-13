class Solution(object):
    def leftRightDifference(self, nums):
        if len(nums)< 2:
            return [0]
        total_sum = sum(nums)
        left_sum = 0
        output = []

        for num in nums:
            total_sum = total_sum - num
            output.append(abs(left_sum - total_sum))
            left_sum = left_sum + num
    
        return output