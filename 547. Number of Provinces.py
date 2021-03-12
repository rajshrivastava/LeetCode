class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def visitComponent(i):
            if i in visited:
                return
            
            visited.add(i)
            
            for j in range(n):
                if M[i][j] == 1:
                    visitComponent(j)
                    
        n = len(M)
        visited = set()
        n_components = 0
        for i in range(n):
            if i not in visited:
                n_components += 1
                visitComponent(i)
        return n_components
