class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def isOverlap(a1,a2,b1,b2):
            if a1<b1:
                return a2 > b1
            else:
                return b2 > a1
                
        if (rec1[0] == rec1[2] or rec1[1] == rec1[3] or \
            rec2[0] == rec2[2] or rec2[1] == rec2[3]):
            return False
        return isOverlap(rec1[0], rec1[2], rec2[0], rec2[2]) and isOverlap(rec1[1], rec1[3], rec2[1], rec2[3])
