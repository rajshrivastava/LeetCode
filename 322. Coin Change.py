class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:        
        val_minCoins = [float('inf')]*(amount+1)
        val_minCoins[0]=0
        
        for coin in coins:
            for i in range(coin, amount+1):  
                val_minCoins[i] = min(val_minCoins[i], 1+val_minCoins[i-coin])
        if val_minCoins[amount]!=float('inf'):
            return val_minCoins[amount]
        else:
            return -1
            
        
