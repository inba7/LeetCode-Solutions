class Solution(object):
    def equalPairs(self, grid):
        row_map = {}
        for row in grid:
            row_tuple = tuple(row)
            if row_tuple in row_map:
                row_map[row_tuple] += 1
            else:
                row_map[row_tuple] = 1
        counter = 0
        for col in zip(*grid):
            if col in row_map:
                counter += row_map[col]
        return counter