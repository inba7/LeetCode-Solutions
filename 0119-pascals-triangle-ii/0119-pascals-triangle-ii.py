class Solution(object):
    def getRow(self, rowIndex):
        Output = [1]
        for X in range(rowIndex):
            Output.append(Output[X]*(rowIndex-X)//(X+1))
        return Output