class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        Sum, Freq = 0, 0
        for Num in range(len(arr)):
            Freq = Freq-(Num+1)//2 + (len(arr)-Num+1)//2
            Sum += Freq*arr[Num]
        return Sum
