class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def leastCost(i):
            if i in dp:
                return dp[i]
            
            if i >=n:
                return 0
            
            oneDay = costs[0] + leastCost(i+1)
            
            j = i
            while j < n and days[j] <= days[i]+6:
                j+=1
            if j < n:
                j-=1
            oneWeek = costs[1] + leastCost(j+1)
            
            j = i
            while j < n and days[j] <= days[i]+29:
                j+=1
            if j < n:
                j-=1
            oneMonth = costs[2] + leastCost(j+1)
            
            dp[i] = min(oneDay, oneWeek, oneMonth)
            return dp[i]
        
        dp = dict()
        lastDay = days[-1]
        n = len(days)
        return leastCost(0)
