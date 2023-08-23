class Solution(object):
    def search(self, nums, Target):
        Left, Right = 0, len(nums)-1
        while Left <= Right:
            Mid = (Left+Right)//2
            if nums[Mid] == Target:
                return Mid
            elif nums[Mid] > Target:
                Right = Mid-1
            else:
                Left = Mid+1
        return -1