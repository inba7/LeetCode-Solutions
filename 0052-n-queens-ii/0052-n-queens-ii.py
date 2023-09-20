class Solution:
    def totalNQueens(self, n):
        def safe(row,col,same_row,left_up,left_down):
            if row in same_row:
                return False
            if (n-1+col-row) in left_up:
                return False
            if (row+col) in left_down:
                return False
            return True
        
        def solve(c,board,same_row,left_up,left_down):
            if c==n:
                ans.append(board[:])
                return 
            for i in range(n):
                if safe(i,c,same_row,left_up,left_down):
                    board[i]=board[i][:c]+'Q'+board[i][c+1:]
                    same_row.add(i)
                    left_up.add(n-1+c-i)
                    left_down.add(i+c)
                    solve(c+1,board,same_row,left_up,left_down)
                    same_row.remove(i)
                    left_up.remove(n-1+c-i)
                    left_down.remove(i+c)
                    board[i]=board[i][:c]+'.'+board[i][c+1:]
                    
        board=['.'*n for _ in range(n)]
        same_row=set()
        left_up=set()
        left_down=set()
        ans=[]
        solve(0,board,same_row,left_up,left_down)
        return len(ans)