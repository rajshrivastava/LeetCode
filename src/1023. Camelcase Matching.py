class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        result = []
        n_p = len(pattern)
        for query in queries:
            p = 0
            q = 0
            '''
            if query[q] == pattern[p]: increment both
            else:
              if query[q] is lowercase, increment q
              else not possible
            '''
            while p < n_p and q < len(query):
                if query[q] == pattern[p]:
                    q += 1
                    p += 1
                elif query[q].islower():
                    q += 1
                else:
                    break
            if p < len(pattern):
                result.append(False)
            elif q < len(query): 
                result.append(query[q:].islower())
            else:
                result.append(True)
                
        return result
                    
