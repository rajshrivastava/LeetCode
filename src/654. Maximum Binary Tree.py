# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def getMaxIndex(left, right):
            maxIndex = left
            for i in range(left, right+1):
                if nums[i] > nums[maxIndex]:
                    maxIndex = i
            return maxIndex
        
        def getRoot(left, right):
            if left > right:
                return None
            p = getMaxIndex(left, right)
            
            node = TreeNode(nums[p])
            node.left = getRoot(left, p-1)
            node.right = getRoot(p+1, right)
            return node
            
        return getRoot(0, len(nums)-1)        
