class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        value_key = {}
        for i, num in enumerate(nums):
            if target - num in value_key:
                return [value_key[target-num], i]
            value_key[num] = i
        
