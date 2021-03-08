class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        lcs_prev = [0]*(len(B)+1)
        for i in range(len(A)):
            lcs_curr = [0]*(len(B)+1)
            for j in range(1, len(B)+1):
                if A[i] == B[j-1]:
                    lcs_curr[j] = lcs_prev[j-1] + 1
                else:
                    lcs_curr[j] = max(lcs_prev[j], lcs_curr[j-1])
            lcs_prev = lcs_curr
        return lcs_curr[-1]
