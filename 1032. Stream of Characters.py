class Node:
    def __init__(self):
        self.endofWord = False
        self.children = {}
        
class StreamChecker:
    def buildTrie(self, words):
        self.trie = Node()
        for word in set(words):
            word = word[::-1]
            node = self.trie
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = Node()
                node = node.children[ch]
            node.endofWord = True
        
    def __init__(self, words: List[str]):
        self.buildTrie(words)
        self.letters = []
        self.len = 0
                
    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        self.len += 1
        i = self.len - 1
        node = self.trie
        while i >= 0:
            if node.endofWord:
                return True

            if self.letters[i] not in node.children:
                return False
            
            node = node.children[self.letters[i]]
                
            i -= 1
            
        return node.endofWord
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
