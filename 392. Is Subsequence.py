class Solution:
#Recursive solution

#     def isSubsequence(self, s: str, t: str) -> bool:
#         def checkRemaining(i,j):
#             if i == s_len:
#                 return True
#             if j == t_len:
#                 return False

#             if s[i] == t[j]:
#                 i+=1

#             return checkRemaining(i, j+1)
        
#         s_len = len(s)
#         t_len = len(t)
#         return checkRemaining(0,0)
    
#Iterative solution
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        n = len(t)
        for ch in s:
            while(ptr < n) and t[ptr]!=ch:
                ptr+=1
            if ptr == n:
                return False
            ptr += 1
        return True
            
