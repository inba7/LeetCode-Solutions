class Solution(object):
    def longestStrChain(self, words):
        Sorted = sorted(words, key=len)
        DP = {}
        Max = 1
        for Word in Sorted:
            Current = 1
            for n in range(len(Word)):
                X = Word[:n] + Word[n+1:]
                if X in DP:
                    Current = max(Current, DP[X] + 1)
            DP[Word] = Current
            Max = max(Max, Current)
        return Max