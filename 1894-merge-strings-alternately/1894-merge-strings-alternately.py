class Solution(object):
    def mergeAlternately(self, word1, word2):
        Merged = []
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                Merged.append(word1[i])
            if i < len(word2):
                Merged.append(word2[i])

        return "".join(Merged)