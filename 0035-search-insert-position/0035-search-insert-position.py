class Solution(object):
    def searchInsert(self, nums, target):
        start, end = 0, len(nums) - 1
        ans = len(nums) # Default answer when target is greater than all elements
        
        while start <= end:
            mid = (start + end) / 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                ans = mid # Update the answer to the current index
                end = mid - 1
                
        return ans