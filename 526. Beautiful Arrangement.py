class Solution:
    def countArrangement(self, N: int) -> int:
        def getValid(i, usedValues):
            if i > N:
                return 1
            
            count = 0
            for val in range(1, N+1):
                if not usedValues[val] and (val%i==0 or i%val == 0):
                    usedValues[val] = True
                    count += getValid(i+1, usedValues) #trying val in (i+1)th position (1-indexed)
                    usedValues[val] = False
            
            return count
        
        usedValues = [False]*(N+1)
        return getValid(1, usedValues)
