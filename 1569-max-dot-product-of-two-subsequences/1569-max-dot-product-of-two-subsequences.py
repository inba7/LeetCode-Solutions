class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        if max(nums1) < 0 and min(nums2) > 0:
            return max(nums1) * min(nums2)
        
        if min(nums1) > 0 and max(nums2) < 0:
            return min(nums1) * max(nums2)
        
        DP = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1) - 1, -1, -1):
            for j in range(len(nums2) - 1, -1, -1):
                Use = nums1[i] * nums2[j] + DP[i + 1][j + 1]
                DP[i][j] = max(Use, DP[i + 1][j], DP[i][j + 1])
        
        return DP[0][0]