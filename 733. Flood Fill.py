class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        r,c = len(image), len(image[0])
        original_color = image[sr][sc]
        queue =collections.deque([(sr,sc)])
        visited = set()
        while queue:
            x, y = queue.popleft()
            image[x][y] = newColor
            visited.add((x,y))
            for xx, yy in (x-1, y), (x, y+1), (x+1, y), (x, y-1):
                if 0<=xx<r and 0<=yy<c and (xx,yy) not in visited and image[xx][yy] == original_color:
                    queue.append((xx,yy))
        return image
