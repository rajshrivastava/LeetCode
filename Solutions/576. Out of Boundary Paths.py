class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        def isOut(i,j):
            return i<0 or i>=m or j<0 or j>=n
        
        def getWays(i,j, moves):
            if isOut(i,j):
                return 1
            if moves == 0:
                return 0
            
            if (i,j,moves) in moves2ways:
                return moves2ways[(i,j,moves)]
            
            for x,y in zip(dirX, dirY):
                moves2ways[(i,j,moves)] += getWays(i+x, j+y, moves-1)
            # print(moves2ways)
            return moves2ways[(i,j,moves)]
        
        moves2ways = collections.defaultdict(int)
        MAX = pow(10,9)+7
        #anti-clockwise
        dirX = [-1,0,1,0]
        dirY = [0,-1,0,1]
        return getWays(i,j, N)%MAX
