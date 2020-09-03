class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        n = len(S)
        i = 0
        j=n-1
        valid = set(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        while i < j:
            while i<n and S[i] not in valid:
                i+=1
            while j>=0 and S[j] not in valid:
                j-=1
            if i < j:
                S[i], S[j] = S[j], S[i]
                i+=1
                j-=1

        return ('').join(S)
