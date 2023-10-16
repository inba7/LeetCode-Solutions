class Solution(object):
    def getRow(self, rowIndex):
        Output = [1]
        for _ in range(rowIndex):
            Output.append(1)
            for X in range(len(Output)-2, 0, -1):
                Output[X] += Output[X-1]
        return Output