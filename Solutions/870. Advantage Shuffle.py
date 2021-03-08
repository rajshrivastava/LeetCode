class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n=len(A)
        A.sort()
        B_sorted_idxs = sorted(list(range(0,n)), key = lambda x: B[x])
        permuted_A = [-1]*n
        j = 0 #for A -index
        remainingA =  []
        for idx in B_sorted_idxs:
            while(j<n and A[j] <= B[idx]):
                remainingA.append(A[j])
                j += 1
            if j == n:
                break
            else:
                permuted_A[idx] = A[j]
                A[j] = None
                j += 1
        
        j = 0
        for val in remainingA:
            while permuted_A[j] != -1:
                j+=1
            permuted_A[j] = val
            j += 1
        
        return permuted_A
