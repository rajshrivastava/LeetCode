class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #Can be done either using stack (DFS) or queue (BFS)
        
        # queue = collections.deque([0])
        stack = [0]
        n = len(rooms)
        visited = {0}
        count = 0
        
        # while queue:
        while stack:
            # room = queue.popleft()
            room = stack.pop()
            count += 1

            if count == n:
                return True
            
            for nextRoom in rooms[room]:
                if nextRoom not in visited:
                    # queue.append(nextRoom)
                    stack.append(nextRoom)
                    visited.add(nextRoom)
        return False
            
