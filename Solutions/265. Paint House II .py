class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:

        if not costs: return 0
        lower_row = costs[-1]
        k = len(lower_row)
        for i in range(len(costs)-2, -1, -1):
            curr_row = costs[i][:]
            for j in range(k):
                curr_row[j] += min(lower_row[:j] + lower_row[j+1:])
                
            lower_row = curr_row[:]
        # print(lower_row)
        return min(lower_row)



