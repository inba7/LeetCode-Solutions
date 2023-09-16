class Solution(object):
    def minimumEffortPath(self, heights):
        m,n = len(heights), len(heights[0])
        visited = [[False for j in range(n)] for i in range(m)] 
        directions = [(1, 0), (-1,0), (0,1), (0,-1)]
        h = [(0, 0, 0)]
        heapify(h)
        while len(h) > 0:
            height, row, col = heappop(h)
            if visited[row][col]:
                continue
            if row == m-1 and col == n-1:
                return height
            visited[row][col] = True
            for dx, dy in directions:
                x, y = row+dx, col+dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    diff = max(height, abs(heights[row][col]-heights[x][y]))
                    heappush(h, (diff, x, y))
        return -1 