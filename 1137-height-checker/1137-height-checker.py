class Solution(object):
    def heightChecker(self, heights):
        Sorted = sorted(heights)
        Count = 0
        for Idx, Val in enumerate(heights):
            if Val != Sorted[Idx]: Count += 1
        return Count