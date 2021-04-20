class Solution:
    def checkRecord(self, s: str) -> bool:
        l, a = 0,0
        for i, ch in enumerate(s):
            if ch == 'A':
                a+=1
                if a == 2: return False
            elif ch == 'L':
                if s[i:i+3] == 'LLL':
                    return False
        return True
