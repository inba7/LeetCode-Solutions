class Solution(object):
    def shuffle(self, nums, n):
        Out = list()
        for x in range(n):
            Out.append(nums[x])
            Out.append(nums[x+n])
        return Out