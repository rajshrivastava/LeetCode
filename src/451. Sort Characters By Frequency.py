class Solution:
    def frequencySort(self, s: str) -> str:
        counts = collections.Counter(s)
        sorted_counts = sorted(list(counts.items()), key = lambda x: x[1], reverse=True)
        sortedString = []
        for ch, count in sorted_counts:
            sortedString.append(ch*count)
        return ''.join(sortedString)
