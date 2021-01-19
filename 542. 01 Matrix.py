from collections import deque
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         def getDist(i,j, visited):
#             print(i,j, visited)
#             #if not 0<=i<m or not 0<=j<n:
#             if i<0 or i>=m or j<0 or j>=n or (i,j) in visited:
#                 return float('inf')
            
#             print('check', result[1][0])
#             if result[i][j] != None:
#                 return result[i][j]
            
#             if matrix[i][j] == 0:
#                 result[i][j] = 0
#                 return 0
            
#             visited.add((i,j))
#             minDist = float('inf')
#             for dx, dy in [(-1,0), (0,1), (1,0), (0,-1)]:
#                 minDist = min(minDist, 1+getDist(i+dx, j+dy, visited))
            
#             result[i][j] = minDist
#             visited.remove((i,j))
#             return minDist
        
        #using bfs
        m,n = len(matrix), len(matrix[0])
        result = [[float('inf')]*n for _ in range(m)]
        
        queue = deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                    result[i][j] = 0
        
        # while len(queue)>0:
        while queue:
            x,y = queue.popleft()
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_x = x+dx
                new_y = y+dy
                #if  0 <=i<m and 0<=j<n:
                if new_x>=0 and new_x <m and new_y>=0 and new_y<n:
                    if result[new_x][new_y] > result[x][y] + 1:
                        result[new_x][new_y] = result[x][y] + 1
                        queue.append((new_x,new_y))
                                                 
        return result
