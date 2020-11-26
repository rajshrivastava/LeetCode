class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        n = len(nums)
        
        nums = [(i,num) for i, num in enumerate(nums)]
        nums.sort(reverse = True, key = lambda x:x[1])
        
        ranks = [None]*n
        ranks[nums[0][0]] = "Gold Medal"
        if n > 1:
            ranks[nums[1][0]] = "Silver Medal"
        if n > 2:
            ranks[nums[2][0]] = "Bronze Medal"
        
        for i in range(3, n):
            ranks[nums[i][0]] = str(i+1)
            
        return ranks
