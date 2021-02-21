from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None) #this is same as using meoization (dp = {})
        def getMax(left, right):
            # if (left, right) in dp:
            #     return dp[(left, right)]
            
            if right - left == 1:
                return max(piles[left:right+1])

            take_left = piles[left] + max(getMax(left+1, right-1), getMax(left+2, right))
            take_right = piles[right] + max(getMax(left+1, right-1), getMax(left, right-2))
            
            # dp[(left, right)] = max(take_left, take_right)
            # return dp[(left, right)] 
            return max(take_left, take_right)
        
        dp = {}
        return getMax(0, len(piles)-1) > sum(piles)/2
