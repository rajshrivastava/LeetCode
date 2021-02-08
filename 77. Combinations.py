class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def getCombinations(soFar, k, nextNum):
            if k == 0:
                self.result.append(soFar)
                return
            
            for i in range(nextNum, n+1):
                getCombinations(soFar + [i], k-1, i+1)
            
            
        self.result = []
        for num in range(1, n-k+2):
            getCombinations([num], k-1, num+1)
        return self.result
        
