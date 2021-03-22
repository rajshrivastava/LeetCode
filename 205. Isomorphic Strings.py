class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mappings = dict()
        mapped = set()
        for x,y in zip(s, t):
            if x in mappings:
                if mappings[x] != y:
                    return False
            else:
                if y in mapped:
                    return False
                mappings[x] = y
                mapped.add(y)
        return True

