from collections import Counter
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        minRabbits = 0
        counts = Counter(answers)
        
        for key, count in counts.items():
            if key == 0:
                minRabbits += count
            else:
                minRabbits += math.ceil(count/(key+1))*(key+1)
                    
        return minRabbits
