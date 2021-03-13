class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        myDistance_to_target = abs(target[0]) + abs(target[1])

        for x,y in ghosts:
            if abs(target[0] - x) + abs(target[1] - y) <= myDistance_to_target:
                return False

        return True
