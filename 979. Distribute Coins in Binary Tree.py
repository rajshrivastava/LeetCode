# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        def count_Nodes_Coins(node = root):
            nonlocal ops
            if not node:
                return 0 
                        
            left = count_Nodes_Coins(node.left)
            right = count_Nodes_Coins(node.right)
            
            balance = node.val + left + right - 1
                
            ops += abs(balance)
            return balance
        
        ops = 0
        count_Nodes_Coins()
        return ops
