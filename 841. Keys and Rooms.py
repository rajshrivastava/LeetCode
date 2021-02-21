class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = collections.deque([0])
        n = len(rooms)
        visited = {0}
        count = 0
        while queue:
            room = queue.popleft()
            count += 1

            if count == n:
                return True
            
            for nextRoom in rooms[room]:
                if nextRoom not in visited:
                    queue.append(nextRoom)
                    visited.add(nextRoom)
        return False
            
