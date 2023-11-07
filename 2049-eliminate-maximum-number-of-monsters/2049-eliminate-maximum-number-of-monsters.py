class Solution:
    def eliminateMaximum(self, dist, speed):
        N = len(dist)
        ArrivalTime = [0] * N

        for Idx in range(N):
            ArrivalTime[Idx] = (dist[Idx] - 1) // speed[Idx]
        ArrivalTime.sort()
        
        for X in range(N):
            if X > ArrivalTime[X]:
                return X

        return N