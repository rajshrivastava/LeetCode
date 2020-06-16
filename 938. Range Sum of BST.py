# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def traverse(node, l ,r):
            if not node:
                return 0
            total = 0
            if node.val >= l:
                total += traverse(node.left, l, r)
            
            total += node.val if node.val>=l and node.val <= r else 0
            
            if node.val <= r:
                total += traverse(node.right, l, r)
            
            return total
        
        return traverse(root, L, R)
