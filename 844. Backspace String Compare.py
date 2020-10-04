class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        # TODO: Write your code here
        def getIdx(i, s):
            backs = 0
            while i >=0:
                if s[i] == '#':
                    backs += 1
                else:
                    if backs > 0:
                        backs -= 1
                    else:
                        break
                i -= 1 
            return i
        
        p1 = len(str1)-1
        p2 = len(str2)-1

        while True:
            p1 = getIdx(p1, str1)
            p2 = getIdx(p2, str2)
            if p1<0 or p2<0:
                break

            if str1[p1] != str2[p2]:
                return False
            
            p1 -= 1
            p2 -= 1

        if p1 >= 0 or p2 >= 0:
            return False

        return True

