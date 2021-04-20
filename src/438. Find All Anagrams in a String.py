# from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, pattern: str) -> List[int]:
        result_indexes = []
        rem_freq = defaultdict(int)
        for ch in pattern:
            rem_freq[ch] += 1
  
        n = len(pattern)
        toMatch = len(rem_freq)
        matched = 0
        window_start = 0
        for window_end in range(len(s)):
            if s[window_end] in rem_freq:
                rem_freq[s[window_end]] -= 1
                if rem_freq[s[window_end]] == 0:
                    matched += 1
                elif rem_freq[s[window_end]] == -1: #try removing by moving matched == n at last
                    matched -= 1

            if window_end >= n:
                if s[window_start] in rem_freq:
                    rem_freq[s[window_start]] += 1
                    if rem_freq[s[window_start]] == 0:
                        matched += 1
                    elif rem_freq[s[window_start]] == 1:
                        matched -= 1

                window_start += 1

            if matched == toMatch:
                result_indexes.append(window_start)

        return result_indexes
