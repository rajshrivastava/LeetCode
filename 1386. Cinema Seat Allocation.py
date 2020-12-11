class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = dict()
        for row, col in reservedSeats:
            if 1 < col < 10:
                seats[row] = seats.get(row, 0) ^ (1<<(9-col))
        count = (n-len(seats))*2
        for sitting in seats.values():
            if sitting & 240 == 0 or sitting & 60 == 0 or sitting & 15 == 0:
                count += 1
        return count
