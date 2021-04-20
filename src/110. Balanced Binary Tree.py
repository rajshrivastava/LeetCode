# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return 1
        left_height = self.isBalanced(root.left)
        right_height = self.isBalanced(root.right)

        if not (left_height and right_height) or abs(left_height - right_height) > 1:
            return False
        return max(left_height, right_height) + 1
        
        return self.isBalanced(root)
