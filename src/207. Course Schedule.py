from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegree = [0]*numCourses
        
        for second, first in prerequisites:
            adjList[first].append(second)
            indegree[second] += 1
        
        queue = deque()
        
        for i, deg in enumerate(indegree):
            if deg == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in adjList[node]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        
        return len(result) == numCourses
