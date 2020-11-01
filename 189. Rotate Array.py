class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        first=-1
        while count < n:
            first +=1
            prevNum = nums[first]
            curr = (first+k)%n
            while curr!=first and count < n-1:
                temp = nums[curr]
                nums[curr] = prevNum
                prevNum = temp    
                curr = (curr+k)%n
                count += 1
            nums[first] = prevNum
            count+=1
