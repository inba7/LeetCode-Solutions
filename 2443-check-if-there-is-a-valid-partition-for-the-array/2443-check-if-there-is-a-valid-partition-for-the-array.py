class Solution(object):
    def validPartition(self, nums):
        A = True
        B = False
        C = nums[0] == nums[1]
        for x in range(2, len(nums)):
            A,B,C,= B,C,B and nums[x] == nums[x-1] or A and (nums[x] == nums[x-1] == nums[x-2] or nums[x] == nums[x-1]+1 == nums[x-2] +2)
        return C