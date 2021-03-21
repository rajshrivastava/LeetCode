# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
#     def getInorder(self, root):
#         if not root:
#             return
#         self.getInorder(root.left)
#         self.inorder.append(root.val)
#         self.getInorder(root.right)
        
#     def __init__(self, root: TreeNode):
#         self.inorder = []
#         self.getInorder(root)
#         self.i = -1
        
#     def next(self) -> int:
#         self.i += 1
#         return self.inorder[self.i]

#     def hasNext(self) -> bool:
#         try:
#             self.inorder[self.i+1]
#         except IndexError:
#             return False
#         else:
#             return True
    
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
            
        
    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
        return val

    def hasNext(self) -> bool:
        return self.stack

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
