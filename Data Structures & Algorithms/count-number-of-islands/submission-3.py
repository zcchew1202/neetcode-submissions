class Solution:
    def is_out_of_bounds(self,r,c,m,n) -> bool:
        if r < 0 or r >= m or c < 0 or c >= n:
            return True
        return False
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        stack = []
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    stack.append((i,j))
                    while stack:
                        r,c = stack.pop()
                        if self.is_out_of_bounds(r,c,m,n) or grid[r][c] != '1':
                                continue
                        grid[r][c] = 'X'
                        for d_r,d_c in directions:
                            nex_r, nex_c = r+d_r,c+d_c
                            stack.append((nex_r,nex_c))
                    count += 1
        return count

