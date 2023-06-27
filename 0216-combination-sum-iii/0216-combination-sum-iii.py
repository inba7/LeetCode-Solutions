class Solution(object):
    def combinationSum3(self, k, n):
        def bp(start, n, k):
            if k == 0 and n == 0:
                return [[]]
            if k == 0 or n < 0:
                return []
            ans = []
            for i in range(start, 10): 
                for bp_ans in bp(i+1, n-i, k-1):
                    ans.append([i] + bp_ans)
            return ans
        return bp(1, n, k)