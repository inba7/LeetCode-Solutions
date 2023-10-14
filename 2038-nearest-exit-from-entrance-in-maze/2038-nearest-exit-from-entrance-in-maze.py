class Solution(object):
    def nearestExit(self, maze, entrance):
        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        start_row, start_col = entrance
        
        queue = collections.deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            if 0 == curr_row or curr_row == rows - 1 or 0 == curr_col or curr_col == cols - 1:
                if curr_row == start_row and curr_col == start_col:
                    pass
                else:
                    return curr_distance

            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]

                if 0 <= next_row < rows and 0 <= next_col < cols \
                    and maze[next_row][next_col] == ".":

                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])
            
        return -1