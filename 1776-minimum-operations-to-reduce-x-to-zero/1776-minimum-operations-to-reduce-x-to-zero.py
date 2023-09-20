class Solution(object):
    def minOperations(self, nums, x):
        Total, N = sum(nums), len(nums)
        Left, Sum, Max = 0, 0, -1
        Target = Total - x

        for Right in range(N):
            Sum += nums[Right]
            while Sum > Target and Left <= Right:
                Sum -= nums[Left]
                Left += 1
            if Sum == Target:
                Max = max(Max, Right - Left + 1)
        
        return N - Max if Max != -1 else -1