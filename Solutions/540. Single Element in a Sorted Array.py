class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        beg, end = 0, n-1
        while beg <= end:
            mid = beg + (end-beg)//2
            if mid-1>=0 and nums[mid] == nums[mid-1]:
                if (end - mid)%2 == 0:
                    end = mid-2
                    
                else:
                    beg = mid+1
            elif mid+1 <n and nums[mid] == nums[mid+1]:
                if (mid - beg)%2 == 0:
                    beg = mid+2
                else:
                    end = mid-1
            else:
                return nums[mid]
        return nums[0]
