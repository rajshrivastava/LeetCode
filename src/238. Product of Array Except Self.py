class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        result[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            result[i] = nums[i]*result[i+1] 

        left_prod = 1 
        for i in range(n-1):
            result[i] = left_prod*result[i+1]
            left_prod *= nums[i] 
        result[n-1] = left_prod
        
        return result
