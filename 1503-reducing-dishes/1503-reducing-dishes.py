class Solution(object):
    def maxSatisfaction(self, satisfaction):
        satisfaction.sort()
        Res = Count = 0
        while satisfaction:
            Curr = satisfaction.pop()
            if Curr + Count < 0: return Res
            Count += Curr
            Res += Count
        return Res