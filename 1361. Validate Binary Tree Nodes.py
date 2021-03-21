from collections import Counter, deque
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 1 node should have inDegree of 0 and other n-1 nodes should have inDegree of 1
        # no cycles (a cycle could exist even when above is satisfied - when there are multiple graph components)
        
        inDegree = [0]*n
        
        for c1, c2 in zip(leftChild, rightChild):
            if c1 != -1: inDegree[c1] += 1
            if c2 != -1: inDegree[c2] += 1
            
        inDegree_count = Counter(inDegree)
        if inDegree_count[0] != 1 or inDegree_count[1] != n-1:
            return False
        
        for i in range(n):
            if not inDegree[i]:
                queue = deque([i])
                break
        
        while queue:
            node = queue.pop()
            
            if leftChild[node]!=-1:
                inDegree[leftChild[node]] -= 1
                if inDegree[leftChild[node]] == 0:
                    queue.append(leftChild[node])

            if rightChild[node]!=-1:
                inDegree[rightChild[node]] -= 1
                if inDegree[rightChild[node]] == 0:
                    queue.append(rightChild[node])
        return not any(inDegree)
