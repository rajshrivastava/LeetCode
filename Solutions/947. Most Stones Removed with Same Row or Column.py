class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(stones)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
        
        visited = [False]*n
        
        components = 0
        for i in range(n):
            if visited[i]: continue
            components += 1
            
            stack = [i]
            visited[i] = True
            while stack:
                node = stack.pop()
                visited[node] = True
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return n - components
