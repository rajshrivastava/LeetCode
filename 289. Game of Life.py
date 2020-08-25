class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def getAliveNeighbors(i,j):
            neighbor_count = 0
            for x,y in neighbors:
                if 0<=i+x<n and 0<=j+y<m:
                    neighbor_count += board[i+x][j+y]
            return neighbor_count
        
        n = len(board)
        m = len(board[0])
        neighbors = [[0,-1],[0,1],[-1,-1],[-1,0],[-1,1],[1,-1],[1,0],[1,1]]
        next_board = [[-1]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                neighbor_count = getAliveNeighbors(i,j)
                if board[i][j] == 1 and (neighbor_count < 2 or neighbor_count > 3):
                    next_board[i][j] = 0
                elif board[i][j] == 0 and neighbor_count == 3:
                    next_board[i][j] = 1
                else:
                    next_board[i][j] = board[i][j]
        for i in range(n):
            for j in range(m):
                board[i][j] = next_board[i][j]
                        
