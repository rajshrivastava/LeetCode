class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        longest = 0
        beg = 0
        for i, ch in enumerate(s):
            if ch in visited:
                longest = max(longest, i-beg)
                while s[beg]!=ch:
                    visited.remove(s[beg])
                    beg += 1
                visited.remove(s[beg])
                beg += 1
            visited.add(ch)
        
        return max(longest, len(s)-beg)
