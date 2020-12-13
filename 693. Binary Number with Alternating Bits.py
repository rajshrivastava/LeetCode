class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n%2 == 1:
            rem = 1
        else:
            rem = 0
        
        while n > 0 and n%2 == rem:
            n //=2
            rem = 1-rem
        
        return n == 0
        

        
