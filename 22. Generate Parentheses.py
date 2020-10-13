class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def getParen(left, right, soFar):
            if left == n and right == n:
                result.append(soFar)
                return
            
            if left < n:
                getParen(left+1, right, soFar+'(')
                                
            if left > right:
                getParen(left, right+1, soFar+")")

        result = []    

        getParen(0,0,'')
        return result
