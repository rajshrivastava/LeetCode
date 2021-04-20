class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i,n=0,len(nums)
        while i < n :
            if nums[i] != i+1:
                j = nums[i]-1
                if nums[i] == nums[j]:
                    return nums[i]
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i+=1
