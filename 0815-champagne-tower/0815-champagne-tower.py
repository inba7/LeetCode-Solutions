class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        Tower = [[0] * (i + 1) for i in range(query_row + 1)]
        Tower[0][0] = poured

        for Row in range(query_row):
            for Glass in range(len(Tower[Row])):
                Excess = (Tower[Row][Glass] - 1) / 2.0
                if Excess > 0:
                    Tower[Row + 1][Glass] += Excess
                    Tower[Row + 1][Glass + 1] += Excess

        return min(1.0, Tower[query_row][query_glass])