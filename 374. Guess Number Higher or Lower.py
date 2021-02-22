# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        mid = low + (high-low)//2
        res = guess(mid)
        while res != 0:
            if res == -1:
                high = mid-1
            else:
                low = mid + 1
            mid = low + (high-low)//2
            res = guess(mid)
        return mid
        
