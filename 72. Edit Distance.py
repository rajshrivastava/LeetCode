class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def minOps(i, j):
            if (i, j) in dp:
                return dp[(i,j)]
            if i == l1 and j == l2:
                return 0
            elif i == l1 or j == l2:
                return l1-i + l2-j
            
            elif word1[i] == word2[j]:
                leastCount =  minOps(i+1, j+1)
            else:
                leastCount = min(minOps(i+1, j+1), minOps(i+1,j), minOps(i, j+1)) + 1
            dp[(i,j)] = leastCount
            # print(dp)
            return leastCount
            
        dp = dict()
        l1, l2 = len(word1), len(word2)
            
        return minOps(i=0, j=0)
