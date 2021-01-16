# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def getMax(node):
            nonlocal highest
            if not node:
                return 0
            left_max = max(0, getMax(node.left))
            right_max = max(0, getMax(node.right))
            curr_sum = left_max + node.val + right_max
            highest = max(highest, curr_sum)
            
            return max(left_max, right_max) + node.val
        
        highest = -float('inf')
        getMax(root)
        return highest
   
