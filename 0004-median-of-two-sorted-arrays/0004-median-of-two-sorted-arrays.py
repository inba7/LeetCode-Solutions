class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1 += nums2
        nums1.sort()
        mid = len(nums1)//2
        if len(nums1)%2 == 0:
            return (nums1[mid]+nums1[mid-1])*0.5
        else:
            return float(nums1[mid])