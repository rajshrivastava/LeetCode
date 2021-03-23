# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def get_maxDiff(node, smallest, largest):
            if not node:
                return largest-smallest
            
            smallest = min(smallest, node.val)
            largest = max(largest, node.val)
            
            return max(get_maxDiff(node.left, smallest, largest), get_maxDiff(node.right, smallest, largest))
            
        return get_maxDiff(root, smallest=root.val, largest=root.val)

