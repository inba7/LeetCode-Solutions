class Solution(object):
    def maxOperations(self, nums, k):
        Count = 0
        num_operations = 0
        d = {}       
        for num in nums:
            if ((k-num) in d) and (d[k-num] > 0):
                d[k-num] -= 1
                Count += 1
            elif num not in d:
                d[num] = 1
            else:
                d[num] += 1
                
        return Count