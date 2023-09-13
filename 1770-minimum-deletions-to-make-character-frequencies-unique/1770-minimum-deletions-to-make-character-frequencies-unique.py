class Solution(object):
    def minDeletions(self, s):
        Freq = [0] * 26
        for char in s:
            Freq[ord(char)-ord('a')] += 1
        Freq.sort()
        Count = 0
        for i in range(24, -1, -1):
            if Freq[i] == 0:
                break
            if Freq[i] >= Freq[i+1]:
                Prev = Freq[i]
                Freq[i] = max(0, Freq[i+1]-1)
                Count += Prev - Freq[i]
        return Count