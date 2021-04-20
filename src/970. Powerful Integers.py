class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x > 1:
            xx = []
            prod = 1
            while prod <= bound:
                xx.append(prod)
                prod *= x
        else:
            xx=[1]
        
        if y > 1:
            yy = []
            prod = 1
            while prod <= bound:
                yy.append(prod)
                prod *= y
        else:
            yy=[1]
            
        result = set()
        for x in xx:
            for y in yy:
                if x+y > bound:
                    break
                result.add(x+y)
        return list(result)
