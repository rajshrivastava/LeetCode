from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m,n = len(rooms), len(rooms[0])
        queue = deque([(i,j) for i in range(m) for j in range(n) if rooms[i][j] == 0])
        while queue:
            x,y = queue.popleft()
            for xx, yy in (x-1,y), (x,y+1), (x+1,y), (x,y-1):
                if 0<=xx<m and 0<=yy<n and rooms[xx][yy] == 2147483647:
                    rooms[xx][yy] = rooms[x][y]+1
                    queue.append((xx,yy))
        return rooms
