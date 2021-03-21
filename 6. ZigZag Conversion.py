class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['']*numRows
        x = 0
        n = len(s)
        while x<n:
            for i in range(numRows):
                if x>=n:
                    break
                rows[i] += s[x]
                x+=1
            for i in range(numRows-2, 0, -1):
                if x>=n:
                    break
                rows[i] += s[x]
                x+=1
        return ('').join(rows)
