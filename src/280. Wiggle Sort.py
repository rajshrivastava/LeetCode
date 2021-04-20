class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        [3,5,2,1,6,4]
        [3,5,1,6,2,4]
        
        [4,3,2,1]
        [3,4,2,1]
        [6,6,5,6,3,8]
        '''
        def is_correct_order(x, y, isAscending):
            return x <= y if isAscending else x >= y
          
        isAscending = True
        for i in range(1, len(nums)):
            if not is_correct_order(nums[i-1], nums[i], isAscending):
                nums[i-1], nums[i] = nums[i], nums[i-1]
            isAscending = not isAscending
        
        
