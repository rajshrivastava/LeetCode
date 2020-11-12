class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        nums = sorted([x for x,y in points])
        max_ = 0
        for i in range(1,len(nums)):
            max_ = max(max_, nums[i]-nums[i-1])
        return max_
