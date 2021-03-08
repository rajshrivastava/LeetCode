class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        first_occurence = {0:-1}
        mask = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        curr = 0
        longest = 0
        for i, ch in enumerate(s):
            curr ^= mask.get(ch, 0)
            # if curr in first_occurence:
            #     longest = max(longest, i - first_occurence[curr])
            # else:
            #     first_occurence[curr] = i
            first_occurence.setdefault(curr, i)
            longest = max(longest, i - first_occurence[curr])
        return longest
                
