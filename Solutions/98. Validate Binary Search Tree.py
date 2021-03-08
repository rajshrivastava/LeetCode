class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def traverse(node, low, high):
            if not node:
                return True
            
            if node.val <= low or node.val >= high:
                return False
            
            return traverse(node.left, low, node.val) and traverse(node.right, node.val, high)
        
        return traverse(root, -math.inf, math.inf)
