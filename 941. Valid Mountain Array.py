class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False
        
        i=1
        while i<n-1 and arr[i-1]<arr[i]:
            i+=1
        
        if i==1:
            return False
        
        while i<n and arr[i-1]>arr[i]:
            i+=1
        
        return i==n
