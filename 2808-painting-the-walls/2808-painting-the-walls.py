class Solution(object):
    def paintWalls(self, cost, time):
        N = len(cost)
        DP = [0] + [float('inf')] * N
        for C, T in zip(cost, time):
            for j in range(N, 0, -1):
                DP[j] = min(DP[j], DP[max(j-T-1, 0)] + C)
        return DP[N]