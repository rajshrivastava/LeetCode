class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ''
        frequencies = collections.Counter(S)
        heap = []
        for k,v in frequencies.items():
            heapq.heappush(heap, (-v,k))

        highest = -heap[0][0]
        
        if highest > len(S) - highest + 1:
            return ''
        
        v,k = heapq.heappop(heap)
        result = [k]
        v += 1
        if v:
            heapq.heappush(heap, (v, k))
        
        while heap:
            v1, k1 = heapq.heappop(heap)
            if result[-1] == k1:
                v2, k2 = heapq.heappop(heap)
                result.append(k2)
                v2 += 1
                if v2:
                    heapq.heappush(heap, (v2, k2))
                heapq.heappush(heap, (v1, k1))
            else:
                result.append(k1)
                v1+=1
                if v1:
                    heapq.heappush(heap, (v1, k1))
        return ''.join(result)
    
    # Time : O(len(S)*log(k)) or O(len(S)log(26)) = O(len(S)), where k = #distinct characters
