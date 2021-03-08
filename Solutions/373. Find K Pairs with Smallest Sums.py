from heapq import *
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1,n2 = len(nums1), len(nums2)
        if not (n1 and n2): return []
        heap = []
        for i in range(min(n1, k)):
            heappush(heap, (nums1[i]+nums2[0], i, 0))
        
        result = []
        k = min(k, n1*n2)
        while k:
            _, i, j = heappop(heap)
            result.append([nums1[i], nums2[j]])
            
            if j+1<n2:
                heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
            
            k -= 1
        
        return result
