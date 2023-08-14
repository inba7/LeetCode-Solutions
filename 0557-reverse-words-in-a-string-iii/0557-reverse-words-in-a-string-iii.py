class Solution(object):
    def reverseWords(self, s):
        return " ".join([Word[::-1] for Word in s.split()])  