class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_high = [0]*n
        col_high = [0]*n
        for i in range(n):
            row_high[i] = max(grid[i])
            
            col_high[i] = 0
            for j in range(n):
                col_high[i] = max(col_high[i], grid[j][i])
        
        increase = 0
        for i in range(n):
            for j in range(n):
                increase += min(row_high[i], col_high[j]) - grid[i][j]
        
        return increase
