class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(i,j):
            target2 = target - nums[i] - nums[j]
            left = j+1
            right = n-1
            while left < right:
                total = nums[left] + nums[right]
                if total == target2:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif total < target2:
                    left += 1
                else:
                    right -= 1
        
        nums.sort()
        n = len(nums)
        i=0
        result = []
        while i < n-3:
            if i>0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = i+1
            while j < n-2:
                if j > i+1 and nums[j] == nums[j-1]:
                    j+=1
                    continue
                twoSum(i, j)
                j+=1
         
            i += 1    
            
        return result
