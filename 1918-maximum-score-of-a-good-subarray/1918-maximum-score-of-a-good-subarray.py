class Solution(object):
    def maximumScore(self, nums, k):
        Res = Mini = nums[k]
        i = j = k
        N = len(nums)

        while i > 0 or j < N - 1:
            if i == 0:
                j += 1
            elif j == N - 1:
                i -= 1
            elif nums[i - 1] < nums[j + 1]:
                j += 1
            else:
                i -= 1

            Mini = min(Mini, min(nums[i], nums[j]))
            Res = max(Res, Mini * (j - i + 1))

        return Res