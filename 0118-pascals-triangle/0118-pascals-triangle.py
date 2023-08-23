class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        Rows = [[1],[1,1]]
        for num in range(2, numRows):
            NewRow = []
            LastRow = Rows[-1]
            for X in range(len(LastRow) - 1):
                NewRow.append(LastRow[X]+LastRow[X+1])
            NewRow = [1]+NewRow+[1]
            Rows.append(NewRow)
        return Rows