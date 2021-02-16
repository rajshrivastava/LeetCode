class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def findLongest(i, j, prevVal):
            if i<0 or i>=m or j<0 or j>=n or prevVal >= matrix[i][j]:
                return 0
            
            if (i,j) in visited:
                return visited[(i,j)]
            
            longestPath = 0
            for ii, jj in (i, j+1), (i+1, j), (i, j-1), (i-1, j):
                longestPath = max(longestPath, findLongest(ii, jj, matrix[i][j]))
            
            visited[(i,j)] = 1 + longestPath
            return visited[(i,j)]
            
        visited = dict()
        m, n = len(matrix), len(matrix[0])
        longestPath = 0
        for i in range(m):
            for j in range(n):
                longestPath = max(longestPath, findLongest(i, j, -float('inf')))
        return longestPath
