class Solution(object):
    def countConsistentStrings(self, allowed, words):
        Count = 0
        for word in words:
            for char in set(word):
                if char not in set(allowed):
                    Count += 1
                    break
        return len(words) - Count