class Solution:
    def minInsertions_r(self, s: str) -> int:
        def getCount(left, right):
            if right <= left:
                return 0
            
            if (left, right) in memo:
                return memo[(left, right)]
            
            if s[left] == s[right]:
                memo[(left, right)] =  getCount(left+1, right-1)
            else:
                memo[(left, right)] = 1 + min(getCount(left+1, right), getCount(left, right-1))
            
            return memo[(left, right)]
        
        memo = dict()
        return getCount(0, len(s)-1)
    
    def minInsertions(self, s: str) -> int: # tabulation
        n = len(s)
        prev = list(range(n+1))
        for i in range(1, n+1):
            curr = [0]*(n+1)
            curr[0] = i
            for j in range(1, n+1):
                if s_rev[i-1] == s[j-1]:
                    curr[j] =  prev[j-1]
                else:
                    curr[j] = 1 + min(curr[j-1], prev[j])
        prev = curr[:]
        
        return curr[-1]
        
