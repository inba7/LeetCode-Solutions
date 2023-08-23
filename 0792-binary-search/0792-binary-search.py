class Solution(object):
    def search(self, nums, target):
        N = len(nums)-1
        while N > -1:
            if nums[N] == target:
                return N
            N-=1
        return -1