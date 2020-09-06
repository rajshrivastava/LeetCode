class Solution:
    def shortestPalindrome(self, s: str) -> str:
        i=0
        for j in range(len(s) - 1, -1, -1):
            if (s[i] == s[j]):
                i+=1
        
        center = (i-1)/2
        
        i, j = math.floor(center), math.ceil(center)
        while i>=0:
            if s[i] == s[j]:
                i-=1
                j+=1
            else:
                center -= 0.5
                i, j = math.floor(center), math.ceil(center)
        
        return ''.join(s[j:][::-1] + s)
