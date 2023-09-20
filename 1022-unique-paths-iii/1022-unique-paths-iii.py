class Solution(object):
    def dfs(self, grid, x, y, emptyCell):
        if x == -1 or x == len(grid) or y == -1 or y == len(grid[0]) or grid[x][y] == -1:
            return 0
        if grid[x][y] == 2:
            return emptyCell == 0
        grid[x][y] = -1
        walks = (self.dfs(grid, x + 1, y, emptyCell - 1)   
               + self.dfs(grid, x - 1, y, emptyCell - 1)   
               + self.dfs(grid, x, y + 1, emptyCell - 1)   
               + self.dfs(grid, x, y - 1, emptyCell - 1)) 
        grid[x][y] = 0
        return walks
    
    def uniquePathsIII(self, grid):
        emptyCell, xIdx, yIdx = 1, 0, 0
        for i in range (len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == 1:
                    xIdx, yIdx = i, j
                elif grid[i][j] == 0:
                    emptyCell += 1
        return self.dfs(grid, xIdx, yIdx, emptyCell)