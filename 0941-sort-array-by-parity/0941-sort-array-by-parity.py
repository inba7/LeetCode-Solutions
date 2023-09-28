class Solution(object):
    def sortArrayByParity(self, nums):
        Even, Odd = 0, len(nums) - 1
    
        while Even < Odd:
            if nums[Even] % 2 != 0 and nums[Odd] % 2 == 0:
                nums[Even], nums[Odd] = nums[Odd], nums[Even]
            if nums[Even] % 2 == 0:
                Even += 1
            if nums[Odd] % 2 != 0:
                Odd -= 1
        return nums