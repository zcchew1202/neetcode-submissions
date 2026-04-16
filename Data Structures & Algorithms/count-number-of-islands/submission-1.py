class Solution:
    def outOfBounds(self, r,c,nRows,nCols):
        return r < 0 or r >= nRows or c < 0 or c >= nCols
    def numIslands(self, grid: List[List[str]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])
        def dfs(r,c):
            if self.outOfBounds(r,c,nRows,nCols) or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return
        count = 0
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == '1':
                    dfs(r,c)
                    count += 1

        return count