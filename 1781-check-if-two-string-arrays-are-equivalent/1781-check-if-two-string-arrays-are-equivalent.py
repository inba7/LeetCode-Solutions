class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        return ("".join(map(str,word1)) == "".join(map(str,word2)))