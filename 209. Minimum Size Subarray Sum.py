class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums[0] >= target:
            return 1
        left = 0
        subsum = nums[0]
        n = len(nums)
        min_size = n+1
        for right in range(1, n):
            subsum += nums[right]
            if subsum >= target:
                while subsum >= target:
                    subsum -= nums[left]
                    left += 1
                min_size = min(min_size, right-left+2)
        return min_size if min_size <=n else 0
