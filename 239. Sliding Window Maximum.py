class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def addIndex(i):
            if deque and deque[0] == i-k:
                deque.popleft()
            
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop()
                
            deque.append(i)

        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums
        
        deque = collections.deque()
        
        for i in range(k):
            addIndex(i)
            # print(i, deque)
        
        result = []
        result.append(nums[deque[0]])
        
        for i in range(k, len(nums)):
            addIndex(i)
            result.append(nums[deque[0]])
            # print(i, deque)
        
        return result
