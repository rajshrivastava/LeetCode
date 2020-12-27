class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0]*n
        left = 0
        right = sum(nums) - n*nums[0]
        prev = nums[0]
        nums[0] = left + right
        for i in range(1, n):
            diff = nums[i]-prev
            left += i*diff
            right -= (n-i)*diff
            prev = nums[i]
            nums[i] = left + right
        return nums
