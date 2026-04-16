class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for r in range(n):
            seenRow = set()
            for c in range(n):
                if board[r][c] in seenRow:
                    return False
                if board[r][c] != '.':
                    seenRow.add(board[r][c])
        for c in range(n):
            seenCol = set()
            for r in range(n):
                if board[r][c] in seenCol:
                    return False
                if board[r][c] != '.':
                    seenCol.add(board[r][c])
        for square in range(n):
            seenBox = set()
            for r in range(3):
                for c in range(3):
                    row = (square//3) * 3 + r
                    col = (square%3) * 3 + c
                    if board[row][col] in seenBox:
                        return False
                    if board[row][col] != '.':
                        seenBox.add(board[row][col])
        return True
        

