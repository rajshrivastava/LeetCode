class Solution:
    def minWindow(self, s: str, t: str) -> str:
        rem_freq = dict()
        for ch in t:
            if ch not in rem_freq:
                rem_freq[ch] = 0
            rem_freq[ch] += 1
        
        toMatch = len(rem_freq)
        matched = 0
        substring = ''
        leastLen = len(s)+1
        window_start = 0
        for window_end in range(len(s)):
            if s[window_end] in rem_freq:
                rem_freq[s[window_end]] -= 1
                if rem_freq[s[window_end]] == 0:
                    matched += 1
            
            if matched == toMatch:
                while matched == toMatch:
                    if s[window_start] in rem_freq:
                        rem_freq[s[window_start]] += 1
                        if rem_freq[s[window_start]] == 1:
                            matched -= 1
                    window_start += 1
                    
                if window_end - window_start + 2 < leastLen:
                    leastLen = window_end - window_start + 2    
                    substring = s[window_start-1:window_end+1]            
        return substring
