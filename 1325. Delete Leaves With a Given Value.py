# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def checkLeaves(node):
            
            if node.left:
                node.left = checkLeaves(node.left)
            if node.right:
                node.right = checkLeaves(node.right)
            
            if not node.left and not node.right:
                if node.val == target:
                    node = None
                return node
            return node
       
        if root:
            return checkLeaves(root)
        return root
        
