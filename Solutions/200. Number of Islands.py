class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def countIslands(i,j):
            if not 0<=i<m or not 0<=j<n:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = "0"
            for dx, dy in directions:
                countIslands(i+dx, j+dy)
            
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        m,n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    countIslands(i,j)
                    count += 1
        return count
