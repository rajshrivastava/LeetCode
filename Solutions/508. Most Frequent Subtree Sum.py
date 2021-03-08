i# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        def calcSum(node):
            if not node:
                return 0
            
            subSum = node.val + calcSum(node.left) + calcSum(node.right)
            self.subSum_to_freq[subSum] += 1
            
            return subSum
            
        self.subSum_to_freq = collections.defaultdict(int)
        calcSum(root)
        
        result = []
        maxFreq = 0
        for subSum, freq in self.subSum_to_freq.items():
            if freq > maxFreq:
                result = [subSum]
                maxFreq = freq
            elif freq == maxFreq:
                result.append(subSum)
        return result
        
