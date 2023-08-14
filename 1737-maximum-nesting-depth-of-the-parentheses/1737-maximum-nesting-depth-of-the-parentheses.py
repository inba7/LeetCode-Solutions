class Solution(object):
    def maxDepth(self, s):
        Max = {0}
        Count = 0
        for char in s:
            if char == "(":
                Count += 1
                Max.add(Count)
            elif char == ")":
                Count -=1
        return max(Max)