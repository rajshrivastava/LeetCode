class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left, right = 0, n-1
        boats = 0
        while left <= right:
            totalWeight = people[right]
            right-=1
            if right >=left and totalWeight + people[right] <= limit:
                right -= 1
            elif left<=right and totalWeight + people[left] <= limit:
                left += 1
            boats += 1
            # print(left, right, boats)
        return boats
