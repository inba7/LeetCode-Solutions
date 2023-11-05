class Solution(object):
    def getWinner(self, arr, k):
        Max = max(arr)
        if k >= len(arr):
            return Max
        
        CurrWinner = arr[0]  
        CurrStreak = 0 
        
        for i in range(1, len(arr)):
            if CurrWinner > arr[i]:
                CurrStreak += 1
            else:
                CurrStreak = 1 
                CurrWinner = arr[i]  

            if CurrStreak == k or CurrWinner == Max:
                return CurrWinner
        
        return CurrWinner