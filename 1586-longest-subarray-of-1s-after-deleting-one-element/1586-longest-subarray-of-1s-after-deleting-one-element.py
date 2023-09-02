class Solution(object):
    def longestSubarray(self, nums):
        oneRuns = []
        cur=0
        for n in nums+[0]:
            if n==0:
                oneRuns+=[cur]
                cur=0
            else:
                cur+=1

        if len(oneRuns)==1: return max(oneRuns[0]-1,0)        
        else: return max([oneRuns[i]+oneRuns[i+1] for i in range(len(oneRuns)-1)])    