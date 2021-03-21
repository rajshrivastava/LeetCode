class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        adjacency = [set() for _ in range(n)]
        for x,y in connections:
            adjacency[x].add(y)
            adjacency[y].add(x)
        components = 0
        visited = [False]*n
        for i in range(n):
            if visited[i]: continue
            stack = [i]
            components += 1
            while stack:
                x = stack.pop()
                visited[x]=True
                for neighbor in adjacency[x]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
        return components - 1
                
