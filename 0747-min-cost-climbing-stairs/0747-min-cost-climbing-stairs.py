class Solution(object):
    def minCostClimbingStairs(self, cost):
        one = 0
        two = 0
        for i in reversed(cost):
            temp = min(i + one, i + two)
            two = one
            one = temp
        return min(one, two)