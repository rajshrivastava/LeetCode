# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        min_level = 1
        max_val = root.val
        
        current = [root]
        curr_level = 1
        
        while current:
            total = 0
            children = []
            for node in current:
                total += node.val
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            
            if total > max_val:
                max_val = total
                min_level = curr_level
            
            curr_level += 1
            current = children
            
        return min_level
