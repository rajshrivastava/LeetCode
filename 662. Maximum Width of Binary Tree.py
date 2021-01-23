# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        maxWidth = 1
        curr = [(root,1)]
        
        while curr:
            children = []
            leftest = float('inf')
            rightest = -float('inf')
            for node_pos in curr:
                node, pos = node_pos
                if node.left:
                    children.append((node.left, pos*2))
                    leftest = min(leftest, pos*2)
                    rightest = max(rightest, pos*2)
                if node.right:
                    children.append((node.right, pos*2 + 1))
                    leftest = min(leftest, pos*2+1)
                    rightest = max(rightest, pos*2 + 1)
            maxWidth = max(maxWidth, rightest-leftest+1)
            curr = children
            # print(leftest, rightest)
        return maxWidth
                
