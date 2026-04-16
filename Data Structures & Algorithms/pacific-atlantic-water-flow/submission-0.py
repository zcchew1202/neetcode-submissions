class Solution:
    def isOutOfBounds(self,r,c,nRows,nCols):
        return r < 0 or c < 0 or r >= nRows or c >= nCols
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nRows, nCols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visit,prevHeight):
            if self.isOutOfBounds(r,c,nRows,nCols) or (r,c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
        
        for c in range(nCols):
            dfs(0, c, pac, heights[0][c])
            dfs(nRows-1, c, atl, heights[nRows-1][c])
        
        for r in range(nRows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, nCols-1, atl, heights[r][nCols-1])
        res = []
        for r in range(nRows):
            for c in range(nCols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])

        return res