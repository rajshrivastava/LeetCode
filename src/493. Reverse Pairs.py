class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(left, mid, right):
            p1, p2 = left, mid+1
            while p1 <= mid and p2 <=right:
                if nums[p1] > nums[p2]*2:
                    self.count += mid-p1+1
                    p2+=1
                else:
                    p1+=1
            nums[left:right+1] = sorted(nums[left:right+1])
            
        def merge_count(left, right):
            if left >= right:
                return
            
            mid = left+(right-left)//2
            merge_count(left, mid)
            merge_count(mid+1, right)
            merge(left, mid, right)

        self.count = 0
        merge_count(0, len(nums)-1)
        return self.count
