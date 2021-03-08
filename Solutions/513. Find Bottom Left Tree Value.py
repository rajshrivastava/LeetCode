# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        current = [root]
        while True:
            children = []
            for node in current:
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            
            if not children:
                return current[0].val
            else:
                current = children
