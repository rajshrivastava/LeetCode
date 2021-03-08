class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def nextI(i):
            return (i + nums[i])%n
                  
        n = len(nums)
        for i in range(n):
            slow, fast = i, i
            if nums[i] > 0:
                while nums[nextI(fast)] > 0 and nums[nextI(nextI(fast))] > 0:
                    slow = nextI(slow)
                    fast = nextI(nextI(fast))
                    if slow == fast:
                        if slow == nextI(slow):
                            break
                        return True

            else:
                while nums[nextI(fast)] < 0 and nums[nextI(nextI(fast))] < 0:
                    slow = nextI(slow)
                    fast = nextI(nextI(fast))
                    if slow == fast:
                        if slow == nextI(slow):
                            break
                        return True

        return False
            
