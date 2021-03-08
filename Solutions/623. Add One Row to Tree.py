# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            newRoot = TreeNode(v)
            newRoot.left = root
            return newRoot
        
        current = [root]
        while current and d > 2:
            children = []
            for node in current:
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            current = children
            d-=1
        
        for node in current:
            x = TreeNode(v)
            x.left = node.left
            node.left = x
            
            x = TreeNode(v)
            x.right = node.right
            node.right = x
        
        return root
        
