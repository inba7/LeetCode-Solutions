class Solution(object):
    def findMinArrowShots(self, points):
        points.sort()
        Arrows = 1
        PrevEnd = points[0][1]

        if len(points) > 1:
            for Start, End in points[1:]:
                if PrevEnd >= Start:
                    PrevEnd = min(PrevEnd, End)
                else:
                    Arrows += 1
                    PrevEnd = End
        return Arrows