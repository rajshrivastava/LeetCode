class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        req_freq = n/4
        
        curr = arr[0]
        freq = 1
        for i in range(1, n):
            if arr[i] == arr[i-1]:
                freq += 1
                if freq > req_freq:
                    return arr[i]
            else:
                freq = 1   
        return arr[0]1
