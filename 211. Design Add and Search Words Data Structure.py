class TrieNode():
    def __init__(self):
        self.children = dict()
        self.endOfWord = False
        
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        ptr = self.trie
        for ch in word:
            if ch not in ptr.children:
                ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]
        ptr.endOfWord = True

    def search(self, word: str) -> bool:
        def searchSubWord(ptr, word):
            if not word:
                return ptr.endOfWord
            
            if word[0] in ptr.children:
                return searchSubWord(ptr.children[word[0]], word[1:])
            
            elif word[0] == '.':
                return any(searchSubWord(ptr.children[key], word[1:]) for key in ptr.children)                      
            
        ptr = self.trie
        return searchSubWord(ptr, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
