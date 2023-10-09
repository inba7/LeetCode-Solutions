class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        maxSeq = 0
        starts = [-1]
        for i in range(len(text2)):
            end = len(text1) - 1
            k = len(starts) - 1
            while k >= 0:
                j = starts[k] + 1
                while j < end:
                    if text1[j] == text2[i]:
                        break
                    j += 1

                if j < len(text1) and text1[j] == text2[i]:
                    if k == len(starts) - 1:
                        starts.append(j)
                    else:
                        starts[k + 1] = j
                end = starts[k]
                k -= 1

        return len(starts) - 1