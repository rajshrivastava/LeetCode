class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N==0: return 1
        n = math.floor(math.log(N,2)) + 1
        return N^((2**n)-1)
