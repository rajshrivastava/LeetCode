class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        inf = float('inf')
        n = len(jobDifficulty)
        highest = jobDifficulty[0]
        prev = [highest]
        for i in range(1, len(jobDifficulty)):
            prev.append(max(prev[i-1], jobDifficulty[i]))
        
        for i in range(1, d): #repeat for d-1 days
            curr = [inf]*n
            for j in range(i, n): #for each position in a day
                curr_day_difficulty = jobDifficulty[j]
                curr[j] = curr_day_difficulty + prev[j-1]
                for k in range(j, -1, -1): #for each combination
                    if jobDifficulty[k] > curr_day_difficulty:
                        curr_day_difficulty = jobDifficulty[k]
                    curr[j] = min(curr[j], curr_day_difficulty + prev[k-1])
                    
            prev = curr
        
        return prev[-1] if prev[-1] <inf else -1
            
