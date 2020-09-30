class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        left = 0
        prod=1
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <len(nums):
                prod /=nums[left]
                left+=1
            
            count += right-left + 1
        return count
