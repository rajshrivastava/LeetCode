class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        nA,nB = len(A), len(B)
        grid = [[0]*(nB+1) for _ in range(nA+1)]
       
        longest = 0
        for i in range(nA):
            for j in range(nB):
                if A[i] == B[j]:
                    grid[i][j] = grid[i-1][j-1] + 1
                    longest = max(longest, grid[i][j])    

        return longest
