class Solution:
    def canCross(self, stones: List[int]) -> bool:
        pos_units = dict()
        for stone in stones:
            pos_units[stone] = set()
        pos_units[0].add(0)
        for pos in stones:
            for k in pos_units[pos]:
                p = max(k -1, 1)
                if pos+p in pos_units:
                    pos_units[pos+p].add(p)
                p = max(k, 1)
                if pos+p in pos_units:
                    pos_units[pos+p].add(p)
                if pos + k+1 in pos_units:
                    pos_units[pos+k+1].add(k+1)

        return bool(pos_units[stones[-1]])
