class Solution(object):
    def largestAltitude(self, gain):
        maxHigh, high = 0, 0
        for i in gain:
            high += i
            if high > maxHigh: 
                maxHigh = high
        return maxHigh