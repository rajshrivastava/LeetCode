class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        count  = [0,0]
        
        maxCount = 0
        longest = 0
        window_start = 0
        for window_end in range(len(arr)):
            count[arr[window_end]] += 1
            maxCount = max(maxCount, count[1])

            if window_end - window_start + 1 - maxCount > k:
                count[arr[window_start]] -= 1
                window_start += 1

            longest = max(longest, window_end -window_start +1)

        return longest
