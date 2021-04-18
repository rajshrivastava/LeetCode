class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                block = set()
                for ii in range(i,i+3):
                    for jj in range(j,j+3):
                        if board[ii][jj] == '.':
                            continue
                        val = int(board[ii][jj])
                        if val in block or val in rows[ii] or val in columns[jj]:
                            return False
                        block.add(val)
                        rows[ii].add(val)
                        columns[jj].add(val)
        return True
