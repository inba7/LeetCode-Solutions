class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        
        DP = [[0] * (n+1) for row in range(m+1)]
        for i in range(1, m+1):
            DP[i][0] = i
        for j in range(1, n+1):
            DP[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i-1][j-1], DP[i-1][j], DP[i][j-1]) + 1
        return DP[m][n]