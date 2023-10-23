class Solution(object):
    def isPowerOfFour(self, n):
        if n <= 0: return False
        LogBase4 = math.log(n, 4)
        return LogBase4 == int(LogBase4)