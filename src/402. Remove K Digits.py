class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if not num:
            return ''
        
        stack = [num[0]]
        for d in num[1:]:
            while stack and d < stack[-1] and k > 0:
                stack.pop()
                k -= 1
            stack.append(d)
        if k > 0:
            stack = stack[:-k]
        
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
                    
        stack = ''.join(stack[i:])
        return stack if stack else "0"
                
