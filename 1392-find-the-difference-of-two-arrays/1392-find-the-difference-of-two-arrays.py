class Solution(object):
    def findDifference(self, nums1, nums2):
        a,b=set(nums1),set(nums2)
        return [list(a-b),list(b-a)]