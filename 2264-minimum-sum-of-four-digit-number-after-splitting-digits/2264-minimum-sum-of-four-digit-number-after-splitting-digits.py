class Solution(object):
    def minimumSum(self, num):
        Nums = sorted(map(int, str(num)))
        return Nums[0]*10 + Nums[1]*10 + Nums[2] + Nums[3]