class Solution(object):
    def isSubsequence(self, s, t):
        counter = 0
        if(len(s) == 0):
            return True
        for i in t:
            if i == s[counter]:
                counter+=1
            if(counter == len(s)):
                return True

        return False