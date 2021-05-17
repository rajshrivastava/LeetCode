class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        def stoping_node(x, y):
            return x < 0 or x >= rows or y < 0 or y >= cols or maze[x][y] == 1

        def get_neighbors(x, y):
            neighbors = []
            for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
                xx, yy = x, y
                while not stoping_node(xx+dx, yy+dy):
                    xx += dx
                    yy += dy
                neighbors.append([xx,yy])
            return neighbors
            
        rows, cols = len(maze), len(maze[0])
        queue = collections.deque([start])
        visited = set()
        while queue:
            x, y = queue.popleft()
            if [x,y] == destination:
                return True
            visited.add((x,y))
            for xx, yy in get_neighbors(x,y):
                if (xx, yy) not in visited:
                    queue.append([xx,yy])
        return False
