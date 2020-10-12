class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def getSubsets(i, soFar):
            nonlocal result
            result.append(soFar)
            for j in range(i+1, n):
                getSubsets(j, soFar + [nums[j]])
        
        n = len(nums)
        result = []
        getSubsets(-1,[])
        return result
