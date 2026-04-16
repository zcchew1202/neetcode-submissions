class Solution:
    def dfs(self, grid, node, count):
        nRows = len(grid)
        nCols = len(grid[0])
        if grid[node[0]][node[1]] == '0':
            return count
        if grid[node[0]][node[1]] == '1':
            # mark as visited
            grid[node[0]][node[1]] = '0'
        if node[0] + 1 < nRows:
            self.dfs(grid,(node[0]+1, node[1]),count)
        if node[0] - 1 >= 0:
            self.dfs(grid,(node[0]-1, node[1]),count)
        if node[1] + 1 < nCols:
            self.dfs(grid,(node[0], node[1]+1),count)
        if node[1] - 1 >= 0:
            self.dfs(grid,(node[0], node[1]-1),count)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        nRows = len(grid)
        nCols = len(grid[0])
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, (i,j), count)
        return count