class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def findPaths(pathSoFar):
            if pathSoFar[-1] in deadEnds:
                return False
            
            if pathSoFar[-1] == n-1:
                paths.append(pathSoFar)
                return True
            
            pathExists = False
            for neighbor in graph[pathSoFar[-1]]:
                if findPaths(pathSoFar + [neighbor]):
                    pathExists = True
            
            if not pathExists:
                deadEnds.add(pathSoFar[-1])
                return False
            
            return True
            
        n = len(graph)
        deadEnds = set()
        paths = []
        findPaths([0])
        return paths
                
