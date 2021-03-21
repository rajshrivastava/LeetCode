class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def is_valid_mutation(s1, s2):
            diff = 0
            for i in range(8):
                if s1[i] != s2[i]:
                    diff += 1
            return diff == 1
            
        queue = collections.deque([(start,0)])
        bank = set(bank)
        while queue:
            curr, count = queue.popleft()
            if curr == end:
                return count
            
            visited = set()
            for mutation in bank:
                if is_valid_mutation(curr, mutation):
                    queue.append((mutation, count+1))
                    visited.add(mutation)
            bank -= visited 
        return -1
