class Solution(object):
    def maxDepth(self, s):
        Count, Max = 0, 0
        for char in s:
            if char == '(':
                Count+=1
                Max = max(Count, Max)
            elif char == ')':
                Count-=1
        return Max