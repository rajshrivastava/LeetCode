class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxDistance = -1
        n = len(seats)
        first1 = seats.index(1)
        last1 = seats[::-1].index(1)
        i = first1 + 1
        while i < n-last1:
            if seats[i] == 0:
                distance = 0
                beg_i = i
                while i<n-last1 and seats[i] == 0:
                    distance += 1
                    i += 1
                if i!=n and beg_i != 0:                
                    distance = math.ceil(distance/2)
                maxDistance = max(maxDistance, distance)
            else:
                i += 1
        return max(maxDistance, first1, last1)
