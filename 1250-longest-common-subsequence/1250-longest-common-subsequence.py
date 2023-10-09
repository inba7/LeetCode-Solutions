class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        l1 = len(text1)
        l2 = len(text2)

        prev = [0 for j in range(l2+1)] 

        for i in range(1,l1+1):
            curr = [0 for x in range(l2+1)] 
            for j in range(1,l2+1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(curr[j-1], prev[j])
                
            prev = curr

        return curr[l2]