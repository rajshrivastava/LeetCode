class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = collections.defaultdict(int)
        repeating_maxCount = 0
        longest = 0
        window_start = 0
        for i in range(len(s)):
            counts[s[i]] += 1
            repeating_maxCount = max(repeating_maxCount, counts[s[i]])
            
            if i - window_start + 1 - repeating_maxCount > k:
                counts[s[window_start]] -= 1
                window_start += 1
            longest = max(longest, i - window_start + 1)

        return longest 
