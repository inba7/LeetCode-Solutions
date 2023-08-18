class Solution(object):
    def longestPalindrome(self, S):
        if len(S)<=1 or S == S[::-1]:
            return S
        else:
            Temp = 1
            Start = 0
            for X in range(1,len(S)):
                Odd = S[X-Temp-1:X+1]
                Even = S[X-Temp:X+1]
                if X-Temp-1>=0 and Odd == Odd[::-1]:
                    Start = X-Temp-1
                    Temp+=2
                    continue
                if Even==Even[::-1]:
                    Start = X-Temp
                    Temp+=1
        return S[Start:Start+Temp]