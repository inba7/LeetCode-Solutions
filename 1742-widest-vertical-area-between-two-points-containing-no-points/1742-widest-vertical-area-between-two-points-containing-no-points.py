class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        Wid = sorted(set([W for [W,L] in points]))
        Max = 0
        for i in range(1, len(Wid)):
            if Max < (Wid[i] - Wid[i-1]):
                Max = Wid[i] - Wid[i-1]
        return Max