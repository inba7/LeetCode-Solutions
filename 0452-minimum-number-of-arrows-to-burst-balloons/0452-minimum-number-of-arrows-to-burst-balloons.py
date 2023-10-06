class Solution(object):
    def findMinArrowShots(self, points):
        points = sorted(points, key = lambda x : x[1])
        PrevEnd = float('-inf')
        Arrows = 0
        for Start, End in points:
            if Start > PrevEnd:
                PrevEnd = End
                Arrows += 1
        return Arrows