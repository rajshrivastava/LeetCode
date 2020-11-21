class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def move(dirIdx, hor, ver):
            if dirIdx == 0:
                ver+=1
            elif dirIdx == 2:
                ver-=1
            elif dirIdx == 3:
                hor -=1
            else:
                hor += 1
            
            return hor, ver
        
        def rotate(L_R, dirIdx):
            if L_R == 'R':
                dirIdx = (dirIdx + 1)%4
            else:
                dirIdx -=1
                if dirIdx == -1:
                    dirIdx = 3
            
            return dirIdx
                
        
        ver = 0
        hor = 0
        dirIdx = 0
        for i in range(4):
            for ch in instructions:
                if ch == 'G':
                    hor, ver = move(dirIdx, hor, ver)
                else:
                    dirIdx = rotate(ch, dirIdx)
        
        return not hor and not ver
