# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:            
        def getForest(node, isRootNode):
            if node:
                if node.val in to_delete:
                    node.left = getForest(node.left, True)
                    node.right = getForest(node.right, True)
                    node=None
                else:
                    node.left = getForest(node.left, False)
                    node.right = getForest(node.right, False)
                    if isRootNode:
                        self.lis.append(node)
            return node
                
        self.lis = []
        to_delete = set(to_delete)
        _ = getForest(root, isRootNode= True)
        return self.lis
