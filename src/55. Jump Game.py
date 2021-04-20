class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums)-2
        while i >=0:
            if nums[i]==0:
                toCross = i
                i-=1
                while i>=0 and nums[i] <= toCross - i:
                    i-=1
                if i < 0:
                    return False
            else:
                i-=1
        return True
        
