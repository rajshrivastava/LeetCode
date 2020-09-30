class Solution:
    def sortedSquares(self, a: List[int]) -> List[int]:
        left, right = 0, len(a)-1
        
        result = [None]*(right+1)
        idx = right
        while left <= right:
            if abs(a[left]) > abs(a[right]):
                result[idx] = a[left]*a[left]
                left+=1
            else:
                result[idx] = a[right]*a[right]
                right-=1
            idx-=1
        return result
