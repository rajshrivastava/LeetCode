class Solution:
    def numTrees(self, n: int) -> int:
        def getUnique(n):
            if n in dp:
                return dp[n]
            if n<=1:
                return 1
            combinations = 0
            for i in range(n):
                combinations += getUnique(i) * getUnique(n-i-1)
            dp[n] = combinations
            return dp[n]
            
        dp = dict()
        return getUnique(n)
