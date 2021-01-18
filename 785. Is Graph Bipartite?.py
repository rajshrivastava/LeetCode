class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def isPossible(curr_node, curr_color):
            if color[curr_node]:
                return color[curr_node] == curr_color
            
            color[curr_node] = curr_color
            
            for neighbor in graph[curr_node]:
                if not isPossible(neighbor, 1-curr_color):
                    return False
            return True
                
        n  = len(graph)
        color = [None]*n
        
        for i in range(n):
            if not color[i]:
                if not isPossible(i, 0):
                    return False
        return True
