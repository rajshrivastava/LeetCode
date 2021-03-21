class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptr1 = 0
        for num in nums:
            if num:
                nums[ptr1] = num
                ptr1 += 1
        for i in range(ptr1, len(nums)):
            nums[i] = 0

