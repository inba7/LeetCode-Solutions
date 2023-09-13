class Solution(object):
    def leftRightDifference(self, nums):
        answer = []
        for i in range(len(nums)):
            answer.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
        return answer