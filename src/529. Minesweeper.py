class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def get_adjacent_mines(x,y):
            n_mines = 0
            for xx, yy in (x-1, y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1):
                if xx >= 0 and xx < n_rows and yy >=0 and yy < n_cols and board[xx][yy] == 'M':
                    n_mines += 1
            return n_mines
                    
        n_rows, n_cols = len(board), len(board[0])
        queue = collections.deque([click])
        while queue:
            x, y = queue.popleft()
            if board[x][y] == 'M':
                board[x][y] = 'X'
                break
            
            elif board[x][y] == 'E':
                n_mines = get_adjacent_mines(x,y)
                if n_mines != 0:
                    board[x][y] = str(n_mines)
                else:
                    board[x][y] = 'B'
                    for xx, yy in (x-1, y-1), (x-1,y), (x-1,y+1), (x,y-1), (x,y+1), (x+1,y-1), (x+1,y), (x+1,y+1):
                        if xx >= 0 and xx < n_rows and yy >=0 and yy < n_cols and board[xx][yy] != 'B':
                            queue.append([xx,yy])
                    
        return board
