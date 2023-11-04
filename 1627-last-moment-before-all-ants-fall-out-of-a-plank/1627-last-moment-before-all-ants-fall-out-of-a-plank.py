class Solution(object):
    def getLastMoment(self, n, left, right):
        time = 0

        for pos in left:
            time = max(time, pos)
        for pos in right:
            time = max(time, n - pos)

        return time