class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        l = n-1
        size = 0
        for i, num in enumerate(nums):
            while stack and num < stack[-1]:
                stack.pop()
                size -= 1
                l = min(l, size)
            stack.append(num)
            size += 1
            
        
        stack = []
        r = 0
        size = 0
        for i in range(n-1, -1, -1):
            while stack and nums[i] > stack[-1]:
                stack.pop()
                size -= 1
                r = max(r, n-1- size)
            stack.append(nums[i])
            size += 1
            
        if r - l > 0:
            return r-l+1
        else:
            return 0
        
        
            
