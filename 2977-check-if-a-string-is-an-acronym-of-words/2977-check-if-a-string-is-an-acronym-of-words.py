class Solution(object):
    def isAcronym(self, words, s):
        return "".join(w[0] for w in words) == s