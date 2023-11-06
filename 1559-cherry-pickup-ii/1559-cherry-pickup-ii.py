class Solution(object):
    def cherryPickup(self, grid):
        height = len(grid)
        width = len(grid[0])
        score = [[[0 for k in xrange(width)] for j in xrange(width)] for i in xrange(height)]
        

        for j in range(0, width):
                for k in range(j+1, width):
                    if(j != k):
                        score[height - 1][j][k] = grid[height-1][j] + grid[height-1][k]
                    else:
                        score[height - 1][j][k] = grid[height-1][j]


        for i in range(height-2, -1 , -1):
            for j in range(0, width):
                for k in range(j, width):
                    if (j != k):
                        best = 0
                        for x in range(j-1, j+2):
                            if(x >= 0 and x < width):
                                for y in range(k-1, k + 2):
                                    if(y >= 0 and y < width):
                                        best = max(best, score[i+1][x][y])
                        
                        score[i][j][k] = grid[i][j]+grid[i][k] + best
                
        return score[0][0][width-1]
