class Solution(object):
    def countConsistentStrings(self, allowed, words):
        Count = 0
        for word in words:
            Flag = 1
            for char in set(word):
                if char not in allowed:
                    Flag = 0
                    break
            Count += Flag
        return Count