class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i1, i2 = 0, 0
        n1, n2 = len(A), len(B)
        
        while i1 < n1 and i2 < n2:
            if A[i1][0] < B[i2][0]:
                if A[i1][1] < B[i2][0]: #if A[i] ends before B[i] starts
                    i1 += 1
                
                elif A[i1][1] < B[i2][1]: #if A[i] ends before B[i] ends
                    x = B[i2][0]
                    y = A[i1][1]
                    result.append([x,y])
                    i1 += 1
                else: #if A[i] ends after B[i] ends
                    result.append(B[i2])
                    i2 += 1
                    
            else: # A[i] starts after B[i] starts
                if A[i1][0] > B[i2][1]: #if A[i] starts after B[i] ends
                    i2+=1
                elif A[i1][1] < B[i2][1]: #if A[i] ends before B[i] ends
                    result.append(A[i1])
                    i1+=1
                else: #if A[i] starts in between B[i]
                    x = A[i1][0]
                    y = B[i2][1]
                    result.append([x,y])
                    i2 += 1
            
        return result
                
