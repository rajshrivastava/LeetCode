class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        ch_word = dict()
        words = set()
        if pattern and not str:
            return None
        
        str = str.split(' ')
        if len(str) != len(pattern):
            return False
        for ch, word in zip(pattern, str):
            if ch in ch_word:
                if ch_word[ch] != word:
                    return False
            else:
                if word in words:
                    return False
                else:
                    ch_word[ch] = word
                    words.add(word)
        return True
