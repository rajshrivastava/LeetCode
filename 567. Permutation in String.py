class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w_size = len(s1)
        n = len(s2)
        
        if n<w_size:
            return False
        
        rem_counts = collections.defaultdict(int)
        
        for i in range(w_size):
            if rem_counts[s1[i]] == -1:
                rem_counts.pop(s1[i])
            else:
                rem_counts[s1[i]] += 1

            if rem_counts[s2[i]] == 1:
                rem_counts.pop(s2[i])
            else:
                rem_counts[s2[i]] -= 1
        
        if not rem_counts:
            return True
        window_start = 0
        for window_end in range(w_size, n):
            if rem_counts[s2[window_end]] == 1:
                rem_counts.pop(s2[window_end])
            else:
                rem_counts[s2[window_end]] -= 1
            
            if rem_counts[s2[window_start]] == -1:
                rem_counts.pop(s2[window_start])
            else:
                rem_counts[s2[window_start]] += 1
            
            if not rem_counts:
                return True
            window_start += 1
        return False
            
        
