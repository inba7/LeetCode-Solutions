class Solution(object):
    def minBitFlips(self, start, goal):
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        if len(start) > len(goal):
            goal = "0" * (len(start)-len(goal)) + goal
        else:
            start = "0" * (len(goal)-len(start)) + start
        Count = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                Count += 1
        return Count