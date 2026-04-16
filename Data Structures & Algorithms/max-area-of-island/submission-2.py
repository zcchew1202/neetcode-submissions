class Solution:
    def isOutOfBounds(self, r,c,nRows,nCols):
        return r < 0 or c < 0 or r >= nRows or c >= nCols
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])
        maxArea = 0
        def dfs(r,c):
            if self.isOutOfBounds(r,c,nRows,nCols) or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return (1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1))


        for r in range(nRows):
            for c in range(nCols):
                maxArea = max(maxArea,dfs(r,c))
        return maxArea
