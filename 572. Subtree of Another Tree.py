# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def areSimilar(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        
        if node1.val != node2.val:
            return False
        
        return self.areSimilar(node1.left, node2.left) and self.areSimilar(node1.right, node2.right)
        
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        
        if not s or not t:
            return False
        
        temp = self.areSimilar(s, t)
        if temp == True:
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
