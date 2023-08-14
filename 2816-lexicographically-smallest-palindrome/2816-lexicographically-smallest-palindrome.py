class Solution(object):
    def makeSmallestPalindrome(self, s):
        s = list(s)
        for x in range(len(s) // 2):
            if s[x] < s[~x]:
                s[~x] = s[x]
            else:
                s[x] = s[~x]
        return ''.join(s) 