class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        l = len(nums1)
        if l%2:
          return nums1[(l-1)/2]
        else:
          return 0.5*(nums1[(l/2)-1]+ nums1[l/2])