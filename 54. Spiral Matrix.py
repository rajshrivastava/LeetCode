class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def offBound(x, y):
            # if any((x < 0, x > m-1, y<0, y>n-1, matrix[x][y]==None)):
            if x < 0 or x > m-1 or y<0 or y>n-1 or matrix[x][y]==None:
                return True
            return False
        
        directions = [(0,1), (1,0), (0,-1),(-1,0)]
        curr_dir = 0
        result = [matrix[0][0]]
        matrix[0][0]=None
        m = len(matrix)
        n = len(matrix[0])
        x,y=0,0
        for i in range(m*n-1):
            dx, dy = directions[curr_dir]
            if offBound(x+dx, y+dy):
                curr_dir = (curr_dir+1)%4
                dx, dy = directions[curr_dir]
            x += dx
            y += dy
            result.append(matrix[x][y])
            matrix[x][y] = None
        return result
            
        