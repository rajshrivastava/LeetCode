class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]
        
        answer = [intervals[0]]        
        
        inserted = False
        for i in range(n):
            if intervals[i][0] <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], intervals[i][1])
            else:
                answer.append(intervals[i])
            
            if inserted == False and newInterval[0] <= answer[-1][1]: #if new interval begins before the current ends
                if newInterval[1] < answer[-1][0]: #if it ends before the current begins, insert it.
                    temp = answer[-1]
                    answer[-1] = newInterval
                    answer.append(temp)

                else: #if it ends after the current begins, then merge.
                    answer[-1][0] = min(answer[-1][0], newInterval[0])
                    answer[-1][1] = max(answer[-1][1], newInterval[1])

                inserted = True
       
        if not inserted:
            answer.append(newInterval)
            
        return answer        
