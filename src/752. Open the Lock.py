class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        queue = collections.deque([('0000',0)])

        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            
            if state in deadends:
                continue
                
            deadends.add(state)
            
            for i in range(4):
                for j in [-1, 1]:
                    next_state = list(state)
                    next_state[i] = str( (int(state[i])+j) % 10)
                    next_state = ''.join(next_state)
                    if next_state not in deadends:
                        queue.append((next_state,turns+1))
                    
        return -1
