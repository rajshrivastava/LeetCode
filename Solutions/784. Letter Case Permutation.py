class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def permute(i,s):
            if i == n:
                permutations.append(s)
                return
            idx = locs[i]
            permute(i+1, s[:idx] + s[idx].lower() + s[idx+1:])
            permute(i+1, s[:idx] + s[idx].upper() + s[idx+1:])
            
        locs = [i for i in range(len(S)) if S[i].isalpha()]
        permutations = []
        n = len(locs)
        permute(0, S)
        return permutations
        
