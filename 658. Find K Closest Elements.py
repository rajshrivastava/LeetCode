class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def getPivot(x):
            left, right = 0, n-1
            while left < right:
                mid = left + (right-left)//2
                
                if arr[mid]  == x:
                    return mid
                elif arr[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
            
        arr = [-float('inf')] + arr + [float('inf')]
        
        n = len(arr)
        p = getPivot(x)
        if arr[p] < x:
            left, right = p, p+1
        else:
            left, right = p-1, p
        
    
        for i in range(k):
            if x - arr[left] < arr[right] - x:
                left -= 1
            elif x - arr[left] > arr[right] - x:
                right += 1
            elif arr[left] < arr[right]:
                left -= 1
            else:
                right += 1
                
        return arr[left+1:right]
                
