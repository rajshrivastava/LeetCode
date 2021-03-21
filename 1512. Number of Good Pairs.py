class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs_count = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    goodPairs_count += 1
        return goodPairs_count
