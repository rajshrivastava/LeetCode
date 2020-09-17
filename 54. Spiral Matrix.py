class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0,1], [1,0],[0,-1],[-1,0]]
        r = len(matrix)
        if r==0:
            return []
        else:
            c = len(matrix[0])
        
        dirIdx = 0
        i,j = 0,0
        seen = [[False] * c for _ in matrix]
        spiral = []
        for _ in range(r*c):
            spiral.append(matrix[i][j]) #append the element to the answer
            seen[i][j] = True
            
            i_ = i + directions[dirIdx][0]
            j_ = j + directions[dirIdx][1]
            
            if i_<0 or i_>r-1 or j_<0 or j_>c-1 or seen[i_][j_]: #collision
                dirIdx = (dirIdx + 1)%4
            
            i += directions[dirIdx][0]
            j += directions[dirIdx][1]
            
        
        return spiral
