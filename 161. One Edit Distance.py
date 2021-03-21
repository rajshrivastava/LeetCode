class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        '''
        1. Traverse from left and right. Stop with first non-matching
        '''
        s_len, t_len = len(s), len(t)
        if abs(s_len - t_len) > 1:
            return False
        
        # traversing from left
        n = min(s_len, t_len)
        left = 0
        while left < n and s[left] == t[left]:
            left += 1
        
        # if the strings are same
        if s_len == t_len == left:
            return False
        elif s_len == t_len:
            return s[left+1:] == t[left+1:]
        else:
            return s[left+1:] == t[left:] if s_len > t_len else s[left:] == t[left+1:]
