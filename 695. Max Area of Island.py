class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def findArea(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0
            
            area = 1
            for ii, jj in [i,j+1], [i+1, j], [i, j-1], [i-1, j]:
                area += findArea(ii, jj)
            return area
            
        m,n = len(grid), len(grid[0])
        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    maxArea = max(maxArea, findArea(i,j))
        return maxArea
