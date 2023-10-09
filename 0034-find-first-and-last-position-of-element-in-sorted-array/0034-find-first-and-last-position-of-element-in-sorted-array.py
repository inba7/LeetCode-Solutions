class Solution(object):
    def searchRange(self, nums, target):
        l = [-1, -1]

        for i in range(len(nums)):
            if nums[i] == target:
                l[0] = i
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                l[1] = i
                break

        return l