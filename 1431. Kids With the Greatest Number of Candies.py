class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        return [candy+extraCandies>=highest for candy in candies]
