class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = collections.defaultdict(int)
        for ch in magazine:
            count[ch]+= 1
        for ch in ransomNote:
            if ch in count and count[ch]>0:
                count[ch] -= 1
            else:
                return False
        return True
