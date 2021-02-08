class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [-1]
        for x in asteroids:
            if x > 0:
                stack.append(x)
            else:
                while stack[-1] > 0 and x + stack[-1] < 0:
                    stack.pop()
                if stack[-1] < 0:
                    stack.append(x)
                elif x + stack[-1] == 0:
                    stack.pop()
        return stack[1:]
