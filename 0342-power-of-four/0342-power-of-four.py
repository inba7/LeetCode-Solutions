class Solution(object):
    def isPowerOfFour(self, n):
        if n == 1: return True
        if n <= 0: return False
        
        LogBase4 = math.log(n) / math.log(4)
        return (LogBase4 == int(LogBase4))