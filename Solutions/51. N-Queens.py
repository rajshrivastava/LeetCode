class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:            
        def findPositions(i, j, attackedColumn = set(), attackedHill = set(), attackedDale = set()):           
            if i == n-1:
                return [[j]]
            
            i += 1
            validPos_list = []
            for k in range(n):
                if not (k in attackedColumn or i+k in attackedHill or i-k in attackedDale):
                    valid = findPositions(i, k, attackedColumn|{k}, attackedHill|{i+k}, attackedDale|{i-k})
                    if valid and len(valid) > 0:
                        validPos_list.extend(valid)
            if len(validPos_list) == 0:
                return None
            return [validPos + [j] for validPos in validPos_list]
                        
        validPos_list = []
        for j in range(n):
            valid = findPositions(0,j, {j}, {j}, {-j})
            if valid:
                validPos_list.extend(valid)
        
        results = []
        for validPos in validPos_list:
            result = []
            for j in validPos:
                row = ['.']*n
                row[j] = 'Q'
                result = [''.join(row)] + result
            results.append(result)
                
        return results
        
        
