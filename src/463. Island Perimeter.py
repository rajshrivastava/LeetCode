class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def findPerimeter(i, j):
            if (i,j) in visited:
                return 0
            
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0:
                return 1
            
            visited.add((i,j))
            sub_perimeter = 0
            for ii, jj in [i,j+1], [i+1, j], [i, j-1], [i-1, j]:
                sub_perimeter += findPerimeter(ii, jj) 
            return sub_perimeter
                
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    return findPerimeter(i, j)
        return 0
