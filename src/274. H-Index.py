class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i=0
        while i < len(citations) and i+1 <= citations[i]:
            i+=1
        return i
