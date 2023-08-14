class Solution(object):
    def makeSmallestPalindrome(self, s):
        Res = ""
        mid = len(s)/2
        for i in range(0, mid):
            Res += min(s[i], s[len(s)-i-1])
        return Res + s[mid] + Res[::-1] if len(s)%2==1 else Res + Res[::-1]