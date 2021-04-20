class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        isModified = False
        if nums[0] > nums[1]:
            nums[0] = nums[1]
            isModified = True
        for i in range(2, len(nums)):
            if nums[i-1] > nums[i]:
                if isModified:
                    return False
                
                isModified = True
                if nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i-2]
                else:
                    nums[i] = nums[i-1]
        return True
        
