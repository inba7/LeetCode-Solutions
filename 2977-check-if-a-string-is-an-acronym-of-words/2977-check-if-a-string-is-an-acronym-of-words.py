class Solution(object):
    def isAcronym(self, words, s):
        return True if "".join(w[0] for w in words) == s else False