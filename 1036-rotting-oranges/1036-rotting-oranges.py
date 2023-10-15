class Solution:
    def orangesRotting(self, grid):
        Queue = deque()
        n, m = len(grid), len(grid[0])
        Count, Time = 0, -1
        Directions = [(1,0), (0,1), (-1,0), (0,-1)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    Count += 1
                elif grid[i][j]==2:
                    Queue.append((i,j))
        while len(Queue) > 0:
            Rotten = []
            while len(Queue)>0:
                Rotten.append(Queue.popleft())
            for Orange in Rotten:
                I, J = Orange
                for A, B in Directions:
                    X, Y = I+A, J+B
                    if 0 <= X < n and 0 <= Y < m and grid[X][Y] == 1:
                        Count -= 1
                        grid[X][Y] = 2
                        Queue.append((X, Y))
            Time += 1
        if not Count:
            return max(Time, 0)
        else:
            return -1