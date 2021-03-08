class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda ele: ele[0]-ele[1])
        totalCost = 0
        for i in range(len(costs)//2):
            totalCost += costs[i][0] + costs[-1-i][1]
        return totalCost
