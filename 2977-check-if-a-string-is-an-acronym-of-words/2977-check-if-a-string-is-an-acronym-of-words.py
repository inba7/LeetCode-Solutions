class Solution(object):
    def isAcronym(self, Words, S):
        return "".join(Word[0] for Word in Words) == S