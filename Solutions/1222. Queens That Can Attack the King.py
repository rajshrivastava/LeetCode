class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        self.canAttack = []
        #queens = set([ tuple(queen) for queen in queens])
        def checkNext(x, y, i,j):
            if  x+i<0 or x+i>7 or y+j<0 or y+j>7:
                return
            #if (x+i,y+j) in queens:
            if [x+i,y+j] in queens:
                self.canAttack.append([x+i,y+j])
                return
            checkNext(x+i, y+j, i, j)
        
        directions = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        for direction in directions:
            checkNext(king[0], king[1], direction[0], direction[1])
        
        return self.canAttack
