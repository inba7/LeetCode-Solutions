class Solution(object):
    def findDifference(self, nums1, nums2):
        n1=set(nums1)
        n2=set(nums2)
        r1=list(set(x for x in nums1 if x not in n2))
        r2=list(set(x for x in nums2 if x not in n1))
        return [r1,r2]