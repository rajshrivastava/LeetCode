"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:        
            queue = deque()
            queue.append(root)

            n = 2
            i = 1
            while queue:
                node = queue.popleft()
                if i == n-1:
                    node.next = None
                    n *= 2
                else:
                    node.next = queue[0]

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                i+=1

        return root
