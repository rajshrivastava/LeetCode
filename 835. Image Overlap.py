class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        def match(beg_i, beg_j):
            count = 0
            low_i = low_j = 0
            high_i = high_j = n
            if beg_i<=0:
                low_i = abs(beg_i)
            else:
                high_i = n - beg_i
            if beg_j<=0:
                low_j = abs(beg_j)
            else:
                high_j = n - beg_j
            for i in range(low_i, high_i):
                for j in range(low_j, high_j):
                    if 0 <= i+beg_i < n and 0 <= j+beg_j < n:
                        if A[i][j] & B[i+beg_i][j+beg_j]:
                            count += 1
            return count
        highest = 0            
        n = len(A)
        for i in range(-n+1, n):
            for j in range(-n+1, n):
                highest = max(highest, match(i,j))
        return highest
