class Solution:
    def isOutOfBounds(self, cell ,limits):
        r, c = cell
        maxRow, maxCol = limits
        return r < 0 or c < 0 or r >= maxRow or c >= maxCol
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numMins = -1
        visited = set()
        q = deque()
        
        def rotOrange(cell):
            r,c = cell
            if self.isOutOfBounds(cell,(rows,cols)) or grid[r][c] != 1:
                return
            q.append(cell)
            grid[r][c] = 2
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        while q:
            numMins += 1
            for neighbor in range(len(q)):
                r,c = q.popleft()
                rotOrange((r+1,c))
                rotOrange((r-1,c))
                rotOrange((r,c+1))
                rotOrange((r,c-1))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        # the grid can also not have any rotten bananas
        return numMins if numMins != -1 else 0





