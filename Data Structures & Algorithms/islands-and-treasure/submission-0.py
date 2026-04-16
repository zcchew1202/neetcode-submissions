class Solution:
    def isOutOfBounds(self, r, c, nRows, nCols):
        return min(r,c) < 0 or r >= nRows or c >= nCols
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nRows = len(grid)
        nCols = len(grid[0])
        INF = 2147483647
        q = deque()
        visited = set()
        def addCell(r,c):
            if self.isOutOfBounds(r,c,nRows,nCols) or (r,c) in visited or grid[r][c] == -1:
                return
            q.append((r,c))
            visited.add((r,c))

            

        # init q with all the treasyre chest locations
        for r in range(nRows):
            for c in range(nCols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        dist = 0
        while q:
            for neighbor in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addCell(r+1,c)
                addCell(r-1,c)
                addCell(r,c+1)
                addCell(r,c-1)

            dist += 1


        



