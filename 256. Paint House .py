class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs: return 0
        lower_row = costs[-1]
        for i in range(len(costs)-2, -1, -1):
            curr_row = costs[i]
            curr_row[0] += min(lower_row[1], lower_row[2])
            curr_row[1] += min(lower_row[0], lower_row[2])
            curr_row[2] += min(lower_row[0], lower_row[1])
            lower_row = curr_row[:]
        return min(lower_row)
        
