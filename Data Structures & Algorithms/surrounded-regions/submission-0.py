class Solution:
    def isOutOfBounds(self, r,c,nRows,nCols):
        return r < 0 or c < 0 or r >= nRows or c >= nCols
    def isInRegion(self,r,c,nRows,nCols):
        return r == 0 or c > 0 or r < nRows - 1 or c < nCols - 1
    def solve(self, board: List[List[str]]) -> None:
        nRows, nCols = len(board), len(board[0])
        def dfs(r,c):
            if self.isOutOfBounds(r,c,nRows,nCols) or board[r][c] != 'O':
                return
            board[r][c] = '#'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(nRows):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][nCols-1] == 'O':
                dfs(r,nCols-1)
        for c in range(nCols):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[nRows-1][c] == 'O':
                dfs(nRows-1,c)
        for r in range(nRows):
            for c in range(nCols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    board[r][c] = 'O'
         


            
            
