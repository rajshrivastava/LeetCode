class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        highestProfit = 0
        for i in range(1, len(prices)):
            highestProfit = max(highestProfit, prices[i] - least)
            least = min(least, prices[i])
        return highestProfit
