class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c= len(matrix[0])
        rows0 = set()
        cols0 = set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows0.add(i)
                    cols0.add(j)
        
        for i in rows0:
            for j in range(c):
                matrix[i][j] = 0
        
        for j in cols0:
            for i in range(r):
                matrix[i][j] = 0
                
