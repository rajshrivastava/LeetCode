class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        m  = n//2
        if n%2==0:
            m -= 1
        
        result = []
        left, right = 0, n-1
        for i in range(k):
            if arr[m] - arr[left] > arr[right] - arr[m]:
                result.append(arr[left])
                left += 1
            else:
                result.append(arr[right])
                right -= 1
        return result
        
            
