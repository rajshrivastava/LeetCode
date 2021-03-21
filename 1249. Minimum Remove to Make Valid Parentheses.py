class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = ['#']
        toRemove = set()
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append((ch,i))
            elif ch == ')':
                if stack[-1][0] != '(':
                    toRemove.add(i)
                else:
                    stack.pop()
        
        for ch, idx in stack[1:]:
            toRemove.add(idx)
        
        result = ''
        for i, ch in enumerate(s):
            if i not in toRemove: result += ch
        return result
        
