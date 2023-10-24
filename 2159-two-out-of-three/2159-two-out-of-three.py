class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        Unique = set(nums1+nums2+nums3)
        Res = []
        for num in Unique:
            Count = 0
            if num in nums1: Count+=1
            if num in nums2: Count+=1
            if num in nums3: Count+=1
            if Count > 1: Res.append(num)
        return Res