class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        beg, end = 0, len(arr)-1
        while beg <= end:
            mid = beg + (end-beg)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid-1] < arr[mid]:
                    beg = mid+1
            else:
                end = mid-1

