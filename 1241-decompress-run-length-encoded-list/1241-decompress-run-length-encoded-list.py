class Solution(object):
    def decompressRLElist(self, nums):
        Out = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                Out.append(nums[i+1])
        return Out