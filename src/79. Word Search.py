class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def isExist(r, c, idx, visited):
            if idx == wordLength:
                return True
            
            if r<0 or r>m-1 or c<0 or c>n-1:
                return False
            
            if visited[r][c]:
                return False
            
            if not board[r][c] == word[idx]:
                return False
            
            visited[r][c] = True
            for x, y in zip(dx, dy):
                if isExist(r+x,c+y, idx+1, visited):
                    return True
            visited[r][c] = False
            return False
            
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        m,n =len(board), len(board[0])
        visited = [[False]*n for i in range(m)]
        wordLength = len(word)
        idx = 0
        for i in range(m):
            for j in range(n):
                if isExist(i, j, idx, visited):
                    return True
        return False
