from heapq import *
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        '''pushing n times takes O(nlogn) time'''
        # heap = []
        # for pos, speed in zip(position, speed):
        #     heappush(heap, (target-pos, speed))
        
        '''heapifying at once takes O(n) time'''
        heap = [(target-pos, s) for pos, s in zip(position, speed)]
        heapify(heap)
        
        
        if not heap:
            return 0
        
        fleets = 1
        front_dist, front_speed = heappop(heap)
        front_time = front_dist/front_speed
        
        while heap:
            dist, speed = heappop(heap)
            if dist/speed > front_time:
                fleets+=1
                front_time = dist/speed
        return fleets
