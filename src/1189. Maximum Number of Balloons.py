class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = dict()
        for ch in text:
            counts[ch] = counts.get(ch, 0) + 1
        counts['l'] = counts.get('l', 0)//2
        counts['o'] = counts.get('o', 0)//2
        min_ = counts.get('b', 0)
        for ch in 'balloon':
            min_ = min(min_, counts.get(ch, 0))
        return min_
