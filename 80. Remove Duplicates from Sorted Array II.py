class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        left = 1
        for right in range(1, n):
            if nums[right] == nums[right-1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[left] = nums[right]
                left += 1
        return left
