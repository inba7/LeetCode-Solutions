class Solution(object):
    def maxScoreWords(self, words, letters, score):
        def BT(i, counts):
            if i == len(words): return 0
            word = Counter(words[i])
            if word == word & counts:
                curr = sum([score[ord(c)-ord("a")] * word[c] for c in word])
                return max(curr+BT(i+1, counts-word), BT(i+1, counts))
            return BT(i + 1, counts)
        return BT(0, Counter(letters))