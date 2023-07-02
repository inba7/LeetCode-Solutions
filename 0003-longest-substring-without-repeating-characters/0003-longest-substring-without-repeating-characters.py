class Solution(object):
    def lengthOfLongestSubstring(self, s):
        Check = {}
        LP, Max = 0, 0
        for RP in range(0, len(s)):
            Char = s[RP]
            if (Char in Check) and (Check[Char] >= LP):
                LP = Check[Char] + 1
            else:
                Max = max(Max, RP-LP+1)
            Check[Char] = RP
        return Max