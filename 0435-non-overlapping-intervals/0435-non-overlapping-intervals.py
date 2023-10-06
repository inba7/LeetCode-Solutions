class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[1])     
        End = float("-inf") 
        Count = 0
        for First, Last in intervals:
            if First < End:
                Count += 1
                continue
            else: End = Last
        return Count