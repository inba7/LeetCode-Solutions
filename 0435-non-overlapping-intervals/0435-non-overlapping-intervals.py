class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        Count = 0
        PrevEnd = intervals[0][1]
        for Start, End in intervals:
            if Start >= PrevEnd:
                PrevEnd = End
            else:
                Count += 1
                PrevEnd = min(PrevEnd, End)
        return Count-1