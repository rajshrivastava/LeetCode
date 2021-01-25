class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        dist1 = sum(distance[start:destination])
        return min(sum(distance)-dist1, dist1)
