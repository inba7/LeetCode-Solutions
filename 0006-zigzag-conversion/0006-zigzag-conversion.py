class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        L = [""]*numRows
        Index, Step = 0, 1
        for Char in s:
            L[Index] += Char
            if Index == 0:
                Step = 1
            elif Index == numRows - 1:
                Step = -1
            Index += Step
        return "".join(L)