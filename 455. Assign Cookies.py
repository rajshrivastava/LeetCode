class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j=0,0
        count = 0
        children = len(g)
        for j in range(len(s)):
            if i == children: break
            if g[i] <= s[j]:
                count += 1
                i+=1
        return count
