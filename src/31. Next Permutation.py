class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        1. Find the first pos i from right such that nums[i] < nums[i+1]
        2. Swap nums[i] with the smallest element larger than nums[i]
        3. Sort nums[i+1:]
        
        Edge cases:
        1. If no number is found in step 1, reverse the array
        2. Empty array, single element -> implicitly handled
        """
        def smallestLarger(i):
            target = nums[i]
            left, right = i+1, len(nums)-1
            ans = -1
            while left <= right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    right = mid - 1
                if nums[mid] > target:
                    ans = mid
                    left = mid+1
                else:
                    right = mid-1
            return ans   
        
        def reverse(begI, lastI):
            while(begI<lastI):
                nums[begI], nums[lastI] = nums[lastI], nums[begI]
                begI += 1
                lastI -= 1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                x = smallestLarger(i)
                nums[i], nums[x] = nums[x], nums[i]
                reverse(i+1, len(nums)-1)
                return
        reverse(0, len(nums)-1)            
