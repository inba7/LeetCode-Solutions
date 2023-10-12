class Solution(object):
    def findInMountainArray(self, target, mountain_arr):
        N = mountain_arr.length()

        PeakIdx = self.FindPeakIdx(1, N-2, mountain_arr)
        IncIdx = self.BinSearch(0, PeakIdx, target, mountain_arr, False)

        if mountain_arr.get(IncIdx) == target:
            return IncIdx
        DescIdx = self.BinSearch(PeakIdx+1, N-1, target, mountain_arr, True)

        if mountain_arr.get(DescIdx) == target:
            return DescIdx
        return -1  

    def FindPeakIdx(self, Low, High, mountainArr):
        while Low != High:
            Mid = Low + (High - Low) // 2
            if mountainArr.get(Mid) < mountainArr.get(Mid + 1):
                Low = Mid + 1 
            else:
                High = Mid  
        return Low  

    def BinSearch(self, Low, High, target, mountainArr, reversed):
        while Low != High:
            Mid = Low + (High - Low) // 2
            if reversed:
                if mountainArr.get(Mid) > target:
                    Low = Mid + 1  
                else:
                    High = Mid  
            else:
                if mountainArr.get(Mid) < target:
                    Low = Mid + 1  
                else:
                    High = Mid  
        return Low