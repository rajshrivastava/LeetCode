class Solution:
    def integerBreak(self, n: int) -> int:
        if n ==2:
            return 1
        if n==3:
            return 2
        dp = [0]*(n+1)
        dp[1],dp[2], dp[3] = 1, 2, 3
        for i in range(4, n+1):
            beg, end = 1, i-1
            high = i
            while beg<=end:
                high = max(high, dp[beg]*dp[end])
                beg+=1
                end-=1
            dp[i] = high
        return dp[n]
