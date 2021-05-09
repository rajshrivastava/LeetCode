class Solution:
    def get_valid_numbers(self, board, x,y):
        valid_numbers = set(map(str, range(1, 10)))

        # check current row and column
        for i in range(9):
            valid_numbers.discard(board[x][i])
            valid_numbers.discard(board[i][y])

        # check current block
        x0, y0 = (x//3)*3, (y//3)*3

        for i in range(x0, x0+3):
            for j in range(y0, y0+3):
                valid_numbers.discard(board[i][j])

        return valid_numbers 

    def get_empty_position(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    return i,j
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        try:
            x, y = self.get_empty_position(board)
        except TypeError as e:
            return True

        for number in self.get_valid_numbers(board, x, y):
            board[x][y] = number
            if self.solveSudoku(board):
                return True
            board[x][y] = '.'

        return False
