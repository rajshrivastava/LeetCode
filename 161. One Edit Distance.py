class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            n1, n2 = n2, n1
            s, t = t, s
            
        if n1 - n2 > 1:
            return False
        
        i = 0
        while i < n2 and s[i] == t[i]:
            i += 1
        
        if i > n2:
            return n1 != n2
        
        i += 1
        if n1 == n2:
            j = i
        else:
            j = i-1
       
        while i < n1 and s[i] == t[j]:
            i += 1
            j += 1
        
        return i == n1
