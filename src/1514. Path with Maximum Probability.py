class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = collections.defaultdict(list)
        for edge, w in zip(edges, succProb):
            u, v = edge
            graph[u].append([v, w])
            graph[v].append([u, w])
        
        pq = [[-1, start]]
        prob = {}
        while pq:
            p, u = heapq.heappop(pq)
            if u == end:
                return -p
            if u in prob:
                continue
            prob[u] = -p
            for v, uv in graph[u]:
                if v not in prob:
                    heapq.heappush(pq, [p*uv, v])
        return 0
        
