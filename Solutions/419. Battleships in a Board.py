class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        r = len(board)
        c = len(board[0])
        onHorShip = -1
        onVertShip = -1
        for i in range(r):
            for j in range(c):
                if board[i][j]=='X':
                    if (i==0 or board[i-1][j] == '.') and (j==0 or board[i][j-1]=='.'):
                        count += 1
        return count
