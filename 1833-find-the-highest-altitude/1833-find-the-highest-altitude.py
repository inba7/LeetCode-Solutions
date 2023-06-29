class Solution(object):
    def largestAltitude(self, gain):
        Alt = [0]
        for i in range(0,len(gain)):
            Alt.append((Alt[i]+gain[i]))
        return max(Alt)
