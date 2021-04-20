class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        
        least = math.inf
        for i in range(4):
            least = min(least, nums[-4+i] - nums[i])
        return least
        
