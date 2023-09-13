class Solution(object):
    def largestLocal(self, grid):
        N = len(grid)
        Rows = [[0] * (N-2) for _ in range(N)]
        for i in range(N):
            for j in range(N-2):
                Rows[i][j] = max(grid[i][j:j+3])
        for i in range(N-2):
            for j in range(N-2):
                Rows[i][j] = max(Rows[i][j], Rows[i+1][j], Rows[i+2][j])
        return Rows[:N-2]