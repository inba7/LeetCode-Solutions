class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        Word1 = Word2 = ""
        for Char in word1:
            Word1 += Char
        for Char in word2:
            Word2 += Char
        return Word1 == Word2