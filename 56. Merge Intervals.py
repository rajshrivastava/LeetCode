class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return []
        intervals.sort(key = lambda x:x[0])
        answer = [intervals[0]]
        for i in range(1, n):
            beg, end = intervals[i]
            if beg <= answer[-1][1]:
                answer[-1][1] = max(end, answer[-1][1])
            else:
                answer.append([beg,end])
        return answer
