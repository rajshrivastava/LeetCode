class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        y = nums[n:]
        for i in range(n-1, 0, -1):
            nums[i*2] = nums[i]
        for i in range(n):
            nums[(i*2) + 1] = y[i]
        return nums
