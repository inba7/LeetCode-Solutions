class Solution(object):
    def closeStrings(self, word1, word2):
        return  sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(word1) == set(word2)