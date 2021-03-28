class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        source_buses, target_buses = [], set()
        for i in range(len(routes)):
            routes[i] = set(routes[i])
            if source in routes[i]:
                source_buses.append(i)
            if target in routes[i]:
                target_buses.add(i)
        
        if not source_buses or not target_buses:
            return -1
        n = len(routes)
        visited = set()
        queue = collections.deque([])
        for i in source_buses:
            queue.append((i,1))
        while queue:
            curr_bus, n_route = queue.popleft()
            if curr_bus in target_buses:
                return n_route
            visited.add(curr_bus)
            for i in range(n):
                if i not in visited and routes[curr_bus].intersection(routes[i]):
                    queue.append((i, n_route+1))
        return -1
        
