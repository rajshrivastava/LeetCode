class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        nums.sort()
        res = set()
        
        for i,v in enumerate(nums[:-2]):
            if i >=1 and v == nums[i-1]:
                continue
                
            dict = {}
            
            for i in nums[i+1:]:
                if i not in dict:
                    dict[-v-i] = 1
                else:
                    res.add((v, -v-i, i))
                    
        return list(map(list,res))
