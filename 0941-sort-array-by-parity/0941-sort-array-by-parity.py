class Solution(object):
    def sortArrayByParity(self, nums):
        even_ptr, odd_ptr = 0, len(nums) - 1
    
        while even_ptr < odd_ptr:
            if nums[even_ptr] % 2 != 0 and nums[odd_ptr] % 2 == 0:
                nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr]

            if nums[even_ptr] % 2 == 0:
                even_ptr += 1

            if nums[odd_ptr] % 2 != 0:
                odd_ptr -= 1

        return nums