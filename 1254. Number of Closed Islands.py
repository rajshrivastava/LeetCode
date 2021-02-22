class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def is_island(i, j):
            if i<0 or i>=m or j<0 or j>=n:
                return False
            
            if grid[i][j] == 1 or (i,j) in visited:
                return True
            
            visited.add((i,j))
            
            answer = True
            for ii, jj in (i, j+1), (i+1, j), (i,j-1), (i-1, j):
                if not is_island(ii, jj):                        
                    answer = False
            return answer
            
            
        visited = set()
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0 and (i,j) not in visited:
                    if is_island(i, j):
                        count += 1
        return count
