class Solution:
    def checkValidString(self, s: str) -> bool:
        least = 0
        highest = 0
        for ch in s:
            if ch == '(':
                least += 1
                highest += 1
            elif ch == ')':
                if highest == 0:
                    return False
                least = max(0, least-1)
                highest = highest-1
            
            else:
                least = max(0, least-1)
                highest = highest + 1
        if least == 0:
            return True
        else:
            return False
