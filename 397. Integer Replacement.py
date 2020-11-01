class Solution:
    def integerReplacement(self, n: int) -> int:
        def minOps(n):
            if n in dp:
                return dp[n]
            if n%2:
                dp[n] = min(minOps(n-1), minOps(n+1)) + 1 
            else:
                dp[n] = minOps(n//2) + 1
            return dp[n]
        
        dp= {}
        dp[1] = 0
        return minOps(n)        
