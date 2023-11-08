class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        if t == 1 and sx == fx and sy == fy:
            return False
 
        return max((abs(sx - fx)), (abs(sy - fy))) <= t