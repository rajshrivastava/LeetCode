# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:            
        if not root:
            return []
            
        idx_vals = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        
        least_idx, highest_idx = float('inf'), -float('inf')
        # queue = [,, (8,1), (4,-1)]
        #least_idx = -1
        #highest_idx = 0
        # idx_vals = {0:[3], -1:[9]}
        while queue:
            node, idx = queue.popleft()
            least_idx = min(least_idx, idx)
            highest_idx = max(highest_idx, idx)
                
            idx_vals[idx].append(node.val)
            if node.left:
                queue.append((node.left, idx-1))
            if node.right:
                queue.append((node.right, idx+1))
            
        print(idx_vals)
        result = []
        
        for i in range(least_idx, highest_idx+1):
            result.append(idx_vals[i])
        
        return result
        
        
        
        
