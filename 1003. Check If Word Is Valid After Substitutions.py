class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        i = 0
        ptr = -1
        while i < len(s):
            if s[i] == 'c':
                if ptr < 1:
                    return False
                
                if stack[ptr] != 'b':
                    return False
                ptr-=1
                if stack[ptr] != 'a':
                    return False
                ptr-=1
            else:
                ptr+=1
                try:
                    stack[ptr]=s[i]
                except IndexError:
                    stack.append(s[i])
            
            i+=1
        
        return ptr==-1
