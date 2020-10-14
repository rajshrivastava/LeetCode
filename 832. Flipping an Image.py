class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        r,c = len(A), len(A[0])
        for i in range(r):
            A[i] = A[i][::-1]
        
        for i in range(r):
            for j in range(c):
                A[i][j]^=1
        
        return A
        
