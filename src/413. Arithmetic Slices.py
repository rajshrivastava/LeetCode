class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        '''
        -5 -2 1 4 5 6 7 9 11
        <3 = 0
        3 -> 1
        4 -> 2+1
        5 -> 3+2+1
        6 -> 4+3+2+1
        n -> n(n+1)/2 -n - (n-1)
          -> (n^2 - 3n + 2)/2
        '''
        def getCount(n):
            return (n**2 - 3*n + 2)/2
        
        n = len(nums)
        if n < 3:
            return 0
        curr_diff = nums[1]-nums[0]
        curr_count = 2
        total_count = 0
        left = 0
        for i in range(2, n):
            if nums[i]-nums[i-1] != curr_diff:
                total_count += getCount(i - left)
                left = i - 1
                curr_diff = nums[i]-nums[i-1]
                curr_count = 2
        total_count += getCount(n - left)
        return int(total_count)
