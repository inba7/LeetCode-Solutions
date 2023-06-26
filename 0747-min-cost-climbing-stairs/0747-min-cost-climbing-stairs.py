class Solution(object):
    def minCostClimbingStairs(self, cost):
        self.table = [-1]*(len(cost)+1)
        self.table[0]=0
        self.table[1]=cost[0]
        for i in range(2,len(cost)+1):
            self.table[i] = cost[i-1]+min(self.table[i-1],self.table[i-2])
        print(self.table)
        return min(self.table[len(cost)],self.table[len(cost)-1])