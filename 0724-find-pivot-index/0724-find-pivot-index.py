class Solution(object):
    def pivotIndex(self, nums):
        left_sum = 0
        right_sum = sum(nums)  
        for i, num in enumerate(nums):
            right_sum -= num
            if left_sum == right_sum:
                return i
            left_sum += num
        return -1