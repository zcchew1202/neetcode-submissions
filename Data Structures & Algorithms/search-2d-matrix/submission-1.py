class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix)-1, len(matrix[0])-1
        top, bot = 0, m
        while top <= bot:
            row = (top+bot)//2
            if matrix[row][n] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break

        if not(top <= bot):
            return False
        
        l, r = 0, n
        row = (top+bot)//2
        while l <= r:
            mid = (l+r)//2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        return False
