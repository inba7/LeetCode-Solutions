class Solution(object):
    def isReachableAtTime(self, sx, sy, fx, fy, t):
        total_distance = max(abs(fx-sx), abs(sy-fy))
        if (total_distance == 0 and t == 1):
            return False
        if (t <= 1 and total_distance > 1):
            return False
        return t >= total_distance