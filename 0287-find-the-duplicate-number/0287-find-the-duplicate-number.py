class Solution(object):
    def findDuplicate(self, nums):
        count = set()
        for i in nums:
            if i in count:
                return i
            else:
                count.add(i)