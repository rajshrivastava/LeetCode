class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        def timeTaken(x):
            if x not in mgr_emp:
                return 0
            
            highestTime = 0
            for sub in mgr_emp[x]:
                highestTime = max(highestTime, timeTaken(sub))
            return informTime[x] + highestTime
            
        mgr_emp = collections.defaultdict(list)
        for i, mgr in enumerate(manager):
            if mgr == -1: continue
            mgr_emp[mgr].append(i)
        
        return timeTaken(headID)
