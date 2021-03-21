class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        high = 0        
        for i in range(len(nums)):
            if nums[i] >= 0:
                curr_high = 0
                x = i
                while nums[x] >= 0:
                    temp = nums[x]
                    nums[x] = -1
                    x = temp
                    curr_high += 1
                high = max(high, curr_high)
        return high
