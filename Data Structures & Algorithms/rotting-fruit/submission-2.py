class Solution:
    def isOutOfBounds(self, r,c,nRows,nCols):
        return r < 0 or c < 0 or r >= nRows or c >= nCols
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nRows = len(grid)
        nCols = len(grid[0])
        visit = set()
        q = deque()
        def rotOrange(r,c):
            if self.isOutOfBounds(r,c,nRows,nCols) or grid[r][c] != 1:
                return
            q.append((r,c))
            grid[r][c] = 2
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
        minutes = -1
        while q:
            minutes += 1
            for neighbor in range(len(q)):
                r,c = q.popleft()
                rotOrange(r+1,c)
                rotOrange(r-1,c)
                rotOrange(r,c+1)
                rotOrange(r,c-1)
                print(minutes)
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 1:
                    return -1
        
        return minutes if minutes != -1 else 0
        
                
