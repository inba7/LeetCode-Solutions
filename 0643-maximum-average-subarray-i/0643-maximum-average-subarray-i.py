class Solution(object):
    def findMaxAverage(self, nums, k):
        s=float(sum(nums[:k]))
        res=s
        for i in range(len(nums)-k):
            s-=(nums[i]-nums[i+k])
            if s > res:
                res=s
        return res/k