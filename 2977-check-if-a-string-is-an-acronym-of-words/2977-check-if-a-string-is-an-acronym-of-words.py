class Solution(object):
    def isAcronym(self, words, s):
        acronym = ""
        for word in words:
            acronym += word[0]
        return s == acronym