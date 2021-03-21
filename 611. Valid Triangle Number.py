class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        nums.sort()
        beg = 0
        while beg < n and nums[beg] == 0: beg += 1
        for i in range(beg, n-2):
            k = i+2
            for j in range(i+1, n-1):
                while k < n and nums[k] < nums[i]+nums[j]:
                    k+=1
                count += k-j-1
        return count
