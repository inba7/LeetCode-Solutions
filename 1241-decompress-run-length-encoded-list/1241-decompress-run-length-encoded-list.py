class Solution(object):
    def decompressRLElist(self, nums):
        Out = []
        for i in range(0, len(nums), 2):
            Freq, Val = nums[i], nums[i+1]
            Temp = [Val] * Freq
            Out.extend(Temp)
        return Out