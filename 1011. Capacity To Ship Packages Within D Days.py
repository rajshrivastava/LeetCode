class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def isValid(capacity):
            day_count = 1
            cum_sum = 0
            for weight in weights:
                cum_sum += weight
                if cum_sum > capacity:
                    day_count += 1
                    cum_sum = weight
            return day_count <= D
            
        low, high = max(weights), sum(weights)
        
        while low <= high:
            mid = low + (high - low)//2
            
            if isValid(mid):
                high = mid-1
            else:
                low = mid+1
                
        return low
