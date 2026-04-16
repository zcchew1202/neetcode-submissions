class Solution:
    def dfs(self, node, grid):
        nRows = len(grid)
        nCols = len(grid[0])
        if grid[node[0]][node[1]] == 0:
            return 0
        grid[node[0]][node[1]] = 0
        area = 1
        if node[0] + 1 < nRows:
            area += self.dfs((node[0]+1,node[1]), grid)
        if node[0] - 1 >= 0:
            area += self.dfs((node[0]-1,node[1]), grid)
        if node[1] + 1 < nCols:
            area += self.dfs((node[0],node[1]+1), grid)
        if node[1] - 1 >= 0:
            area += self.dfs((node[0],node[1]-1), grid)
        return area
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])
        area = 0
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    area = max(area,self.dfs((i,j),grid))
        return area
                
