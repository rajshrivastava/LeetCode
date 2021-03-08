class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        left = 0
        longest = 0
        n = len(arr)
        for right in range(n):
            if arr[right] == 0:
                k-=1
            
            if k < 0:
                while left < n and arr[left] != 0:
                    left += 1
                left += 1
                k = 0
            longest = max(longest, right-left+1)    
            # print(left, right, arr[right], longest, k)

        return longest        
