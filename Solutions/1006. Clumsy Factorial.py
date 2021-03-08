class Solution:
    def clumsy(self, N: int) -> int:
        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 6
        ans = N*(N-1)//(N-2) + (N-3)
        
        N -= 4

        while N >= 4:
            ans -= N*(N-1)//(N-2)
            ans += (N-3)
            N -= 4

        temp = 0
        if N > 0:
            temp -= N
            N -= 1
        if N > 0:
            temp *= N
            N -= 1
        if N > 0:
            temp //= N
        
        return ans + temp
        
