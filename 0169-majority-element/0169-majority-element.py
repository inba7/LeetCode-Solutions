class Solution(object):
    def majorityElement(self, nums):
        Count, Majority = 0, 0
        for i in range(len(nums)):
            if Count == 0 and Majority != nums[i]:
                Majority = nums[i]
                Count += 1
            elif Majority == nums[i]:
                Count += 1
            else:
                Count -= 1
        return Majority