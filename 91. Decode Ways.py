class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        ways = [0]*n
        if s[0] == '0':
            return 0
        
        ways[0] = 1
        
        if n == 1:
            return ways[0]
        
        if s[1] != '0':
            ways[1] = 1
        
        if int(s[:2]) <= 26:
            ways[1] += 1
            
        for i in range(2, n):
            if s[i] != '0':
                ways[i] += ways[i-1]
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                ways[i] += ways[i-2]
        return ways[-1]
