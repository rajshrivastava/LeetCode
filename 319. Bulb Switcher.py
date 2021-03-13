class Solution:
    def bulbSwitch(self, n: int) -> int:
        '''
        <=3 -> 1
        <=8 -> 2
        <=15 -> 3
        use binary search between (1, n/2) to find the largest number which has a square within n
        '''
        if n<=1:
            return n
        left, right = 0, n//2
        while left < right:
            mid = left + (right - left)//2
            if mid*mid == n:
                return mid
            elif mid*mid > n:
                right = mid - 1
            else:
                left = mid + 1
        return left if left*left <= n else left-1
