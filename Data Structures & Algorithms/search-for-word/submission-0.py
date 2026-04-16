class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] *n for _ in range(m)] 
        def dfs(i,j,c):
            if c == len(word):
                return True
            if (i < 0 or i >= m or j < 0 or j >= n or word[c] != board[i][j] or visited[i][j]):
                return False
            visited[i][j] = True
            res = dfs(i-1,j,c+1) or dfs(i+1,j,c+1) or dfs(i,j-1,c+1) or dfs(i,j+1,c+1)
            visited[i][j] = False
            return res
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False