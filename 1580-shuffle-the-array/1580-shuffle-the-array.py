class Solution(object):
    def shuffle(self, nums, n):
        Out = []
        nums1, nums2 = nums[:n], nums[n:n+n]
        for i in range(n):
            Out.append(nums1[i])
            Out.append(nums2[i])
        return Out