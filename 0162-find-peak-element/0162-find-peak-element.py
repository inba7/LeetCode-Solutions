class Solution(object):
    def findPeakElement(self, nums):
        start = 0
        end = len(nums) - 1
        while(start<end):
            mid = start + int((end-start)/2)
            if nums[mid]<nums[mid+1]:
                start = mid+1
            else:
                end = mid
        return start