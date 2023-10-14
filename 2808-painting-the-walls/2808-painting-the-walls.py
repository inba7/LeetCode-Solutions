class Solution(object):
    def paintWalls(self, cost, time):
        N = len(cost)
        DP = [float('inf')] * (N+1) 
        DP[0] = 0 
        for i in range(N):
            for j in range(N, 0, -1):
                DP[j] = min(DP[j], DP[max(j-time[i]-1, 0)] + cost[i])

        return DP[N]