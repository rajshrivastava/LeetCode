class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def getDivision(source, target):
            queue = collections.deque()
            if source in graph:
                queue.append((source, 1))
            visited = set()
            while queue:
                node, ans = queue.popleft()
                visited.add(node)
                if node == target:
                    return ans
                
                for child, val in graph[node].items():
                    if child not in visited:
                        queue.append((child, ans*val))
            
            return -1
            
        
        graph = collections.defaultdict(dict)
        
        for (x, y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1/value

        result = []
        for x, y in queries:
            result.append(getDivision(x, y))
        return result
