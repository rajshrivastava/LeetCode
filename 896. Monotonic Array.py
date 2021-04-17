class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        n = len(A)
        if n == 1:
            return True
        
        i = 1
        while i < n and A[i] == A[i-1]:
            i += 1
        
        if i == n:
            return True
        
        if A[i] > A[i-1]:
            for j in range(i, n):
                if A[j] < A[j-1]:
                    return False
        else:
            for j in range(i, n):
                if A[j] > A[j-1]:
                    return False
        return True
