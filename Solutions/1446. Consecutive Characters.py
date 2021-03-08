class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        maxCount = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count+=1
            else:
                maxCount = max(maxCount, count)
                count = 1
        return max(maxCount, count)
        
