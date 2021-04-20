class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def getMaxGold(i, j, visitedNodes):
            maxGold = 0 
            for neighbor in ((0,1),(0,-1),(1,0),(-1,0)):
                x, y = i+neighbor[0], j+neighbor[1]
                if (x,y) not in visitedNodes and x>=0 and x<r and y>=0 and y<c and grid[x][y]!= 0:
                    maxGold = max(maxGold, getMaxGold(x, y, visitedNodes | {(x,y)}))
    
            return grid[i][j] + maxGold
        
        r = len(grid)
        c = len(grid[0])
        maxGold = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]!=0:
                    maxGold = max(maxGold, getMaxGold(i,j, {(i,j)}))
                
        return maxGold
