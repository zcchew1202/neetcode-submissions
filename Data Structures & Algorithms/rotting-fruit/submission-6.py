class Solution:
    def isOutOfBounds(self, row, col, nRows, nCols):
        return row < 0 or col < 0 or row >= nRows or col >= nCols
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nRows, nCols = len(grid), len(grid[0])
        q = deque()
        visited = set()
        def rotOrange(r,c):
            if self.isOutOfBounds(r, c, nRows, nCols) or (r,c) in visited or grid[r][c] != 1:
                return
            # can't use 2 as visited since we don't excliusively visit rotten cells
            grid[r][c] = 2
            q.append((r,c))
            

        time = -1
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        while q:
            time += 1
            for neighbor in range(len(q)):
                r,c = q.popleft()
                if grid[r][c] == 2:
                    rotOrange(r+1,c)
                    rotOrange(r-1,c)
                    rotOrange(r,c+1)
                    rotOrange(r,c-1)
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 1:
                    return -1
        return time if time != -1 else 0 
        