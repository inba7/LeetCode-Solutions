class Solution(object):
    def heightChecker(self, heights):
        Sorted = heights[:]
        Sorted.sort()
        Count = 0
        for X in range(len(heights)):
            if heights[X] != Sorted[X]: Count += 1
        return Count