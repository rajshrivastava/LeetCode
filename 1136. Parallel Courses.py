from collections import defaultdict
class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        inDegree = [0]*(N+1) #[0,0,0,0,0]
        adjList = defaultdict(list)
        
        for parent, child in relations:
            adjList[parent].append(child)
            inDegree[child] += 1
        
        currLevel = [(i) for i,d in enumerate(inDegree[1:], 1) if d == 0]
        level = 0
        while currLevel: #[]
            nextLevel = []
            for node in currLevel:
                for child in adjList[node]: #child = 4
                    inDegree[child] -= 1
                    if inDegree[child] == 0:
                        nextLevel.append(child)
            
            currLevel = nextLevel
            level += 1
                
        if any(inDegree): return -1 #check cycle
        
        return level
