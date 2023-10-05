class Solution:
    def majorityElement(self, nums):
        result = []
        elements = set(nums)
        for ele in elements:
            if nums.count(ele) > len(nums)//3:
                result.append(ele)
        return result