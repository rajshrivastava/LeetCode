"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = [[root.val]]
        current = [root]
        while current:
            children = []
            children_values = []
            for node in current:
                children.extend(node.children)
                for child in node.children:
                    children_values.append(child.val)
            result.append(children_values)
            current = children
        return result[:-1]
